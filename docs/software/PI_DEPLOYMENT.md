# Raspberry Pi Deployment & Configuration

## Pi 5 Operating System Setup

### Recommended OS Configuration
- **OS**: Raspberry Pi OS Lite (64-bit) - Minimal desktop for performance
- **Storage**: 64GB+ microSD for OS, 1TB+ USB 3.0 SSD for media
- **Cooling**: Essential for Pi 5 - heat sink + small fan recommended
- **Power**: Official Pi 5 USB-C power supply (27W) required

### Initial Pi Setup
```bash
# Enable SSH and configure basics
sudo raspi-config
# 1. Enable SSH
# 2. Expand filesystem  
# 3. Set GPU memory split to 128MB
# 4. Enable hardware acceleration

# Update system
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install -y \
    python3-pip python3-venv \
    vlc python3-vlc \
    lirc \
    git \
    ffmpeg \
    chromium-browser \
    htop \
    screen
```

### Pi 5 Specific Optimizations
```bash
# Add to /boot/config.txt for Pi 5
echo "
# Pi 5 optimizations for video playback
gpu_mem=128
dtoverlay=vc4-kms-v3d,cma-512
max_framebuffers=2

# Enable hardware video decoding
dtoverlay=rpivid-v4l2

# 8-inch display configuration (adjust for your specific LCD)
hdmi_group=2
hdmi_mode=87
hdmi_cvt=1024 768 60 6 0 0 0
hdmi_drive=1

# Audio configuration
dtparam=audio=on
audio_pwm_mode=2
" | sudo tee -a /boot/config.txt
```

## Hardware Interface Setup

### IR Receiver Configuration
```bash
# Install LIRC for IR remote control
sudo apt install lirc

# Configure LIRC - edit /etc/lirc/lirc_options.conf
sudo nano /etc/lirc/lirc_options.conf
# Change:
# driver = devinput
# device = auto
# To:
# driver = default
# device = /dev/lirc0

# Add to /boot/config.txt
echo "dtoverlay=gpio-ir,gpio_pin=18" | sudo tee -a /boot/config.txt

# Test IR receiver
sudo systemctl start lircd
sudo systemctl enable lircd
```

### GPIO Pin Configuration
```python
# src/hardware/gpio_config.py
"""
GPIO pin assignments for Pi Terminal hardware integration
"""

# IR receiver
IR_RECEIVER_PIN = 18

# Control panel buttons (if using Pi Terminal PCB)
BUTTON_PINS = {
    'power': 2,
    'channel_up': 3,
    'channel_down': 4,
    'channel_1': 14,
    'channel_2': 15,
    'channel_3': 16,
    'channel_4': 17,
    'channel_5': 27,
    'channel_6': 22
}

# Status LEDs
LED_PINS = {
    'power': 5,
    'channel_1': 6,
    'channel_2': 13
}

# Audio output (if using GPIO audio)
AUDIO_PINS = {
    'left': 12,
    'right': 13
}
```

### USB SSD Configuration
```bash
# Format and mount USB SSD for media storage
sudo fdisk -l  # Find your SSD (usually /dev/sda)

# Create filesystem
sudo mkfs.ext4 /dev/sda1

# Create mount point
sudo mkdir -p /media/usb

# Add to /etc/fstab for auto-mount
echo "/dev/sda1 /media/usb ext4 defaults,uid=pi,gid=pi 0 2" | sudo tee -a /etc/fstab

# Mount immediately
sudo mount -a

# Verify mount
df -h /media/usb
```

## Display Configuration

### 8-inch LCD Setup (Pi Terminal Compatible)
```bash
# For HJ080IA-01E display (Pi Terminal project)
# Edit /boot/config.txt
sudo nano /boot/config.txt

# Add display-specific settings:
hdmi_group=2
hdmi_mode=87
hdmi_cvt=1024 768 60 6 0 0 0  # 8-inch 4:3 display
hdmi_drive=1
config_hdmi_boost=4

# Disable overscan for clean edges
disable_overscan=1

# Rotate display if needed
display_rotate=0  # 0=normal, 1=90°, 2=180°, 3=270°
```

### Touch Screen Configuration (if applicable)
```bash
# Install touch screen drivers
sudo apt install xinput-calibrator

# Add touch configuration to X11
sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf
```

## Software Deployment

### Application Installation
```bash
# Create application directory
sudo mkdir -p /opt/90s-crt-tv
sudo chown pi:pi /opt/90s-crt-tv

# Clone project
cd /opt/90s-crt-tv
git clone /path/to/your/project .

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Pi-specific packages
pip install RPi.GPIO python-lirc gpiozero
```

### Weather Star 4000+ Setup
```bash
# Install weather channel in weather directory
cd /opt/90s-crt-tv/weather
git clone https://github.com/netbymatt/ws4kp.git

# Install Node.js for weather app
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Setup weather app
cd ws4kp
npm install
npm run build

# Configure for kiosk mode
cp config.sample.json config.json
# Edit config.json with your location
```

### Gaming Channel Setup (Optional)
```bash
# Install RetroPie for gaming channel
cd /home/pi
git clone --depth=1 https://github.com/RetroPie/RetroPie-Setup.git
cd RetroPie-Setup
sudo ./retropie_setup.sh

# Basic install for essential emulators
# Choose: Basic Install from the menu
```

## Service Configuration

### Systemd Service for Auto-Start
```ini
# /etc/systemd/system/90s-crt-tv.service
[Unit]
Description=90s CRT TV Experience
After=network.target sound.service

[Service]
Type=simple
User=pi
Group=pi
WorkingDirectory=/opt/90s-crt-tv
Environment=DISPLAY=:0
Environment=XDG_RUNTIME_DIR=/run/user/1000
ExecStart=/opt/90s-crt-tv/venv/bin/python src/main.py
Restart=always
RestartSec=10

# Performance optimizations
Nice=-5
IOSchedulingClass=1
IOSchedulingPriority=3

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable 90s-crt-tv.service
sudo systemctl start 90s-crt-tv.service

# Check status
sudo systemctl status 90s-crt-tv.service

# View logs
sudo journalctl -u 90s-crt-tv.service -f
```

### Boot Configuration for Kiosk Mode
```bash
# Auto-login configuration
sudo raspi-config
# Choose: Boot Options → Desktop/CLI → Console Autologin

# Start X11 automatically and launch app
# Add to /home/pi/.bashrc
echo "
# Auto-start 90s TV on login
if [ -z \"\$SSH_CLIENT\" ] && [ -z \"\$SSH_TTY\" ]; then
    startx /opt/90s-crt-tv/scripts/start_tv.sh
fi
" >> /home/pi/.bashrc
```

## Performance Optimization

### Video Playback Optimization
```bash
# GPU memory configuration for smooth video
echo "gpu_mem=128" | sudo tee -a /boot/config.txt

# Enable hardware video acceleration
echo "dtoverlay=rpivid-v4l2" | sudo tee -a /boot/config.txt

# VLC optimization settings in application
VLC_ARGS = [
    '--intf', 'dummy',
    '--no-video-title-show',
    '--no-audio-visual',
    '--avcodec-hw=any',           # Hardware acceleration
    '--file-caching=1000',        # Reduce buffer for faster seeking
    '--network-caching=1000',
    '--no-snapshot-preview',
    '--quiet'
]
```

### System Performance Tuning
```bash
# CPU governor for performance
echo "performance" | sudo tee /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

# Add to /etc/rc.local for boot-time optimization
echo "
# Performance optimizations
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo 1 > /proc/sys/vm/overcommit_memory
echo 3 > /proc/sys/vm/drop_caches
" | sudo tee -a /etc/rc.local
```

### Memory Management
```python
# src/utils/pi_optimization.py
import psutil
import gc
import logging

class PiOptimizer:
    """Performance optimizations for Raspberry Pi deployment"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.memory_threshold = 0.85  # Alert when 85% memory used
    
    def optimize_memory(self):
        """Free up system memory when needed"""
        memory_info = psutil.virtual_memory()
        
        if memory_info.percent > self.memory_threshold * 100:
            self.logger.warning(f"High memory usage: {memory_info.percent:.1f}%")
            
            # Force garbage collection
            gc.collect()
            
            # Clear system caches (requires root)
            try:
                with open('/proc/sys/vm/drop_caches', 'w') as f:
                    f.write('3')
                self.logger.info("Cleared system caches")
            except PermissionError:
                pass
    
    def monitor_temperature(self):
        """Monitor Pi temperature and adjust performance"""
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                temp = int(f.read()) / 1000.0
            
            if temp > 70.0:  # Pi is getting hot
                self.logger.warning(f"High temperature: {temp:.1f}°C")
                return True  # Signal to reduce performance
            
            return False
        except FileNotFoundError:
            return False  # Not on Pi
    
    def get_system_stats(self):
        """Get system performance statistics"""
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'temperature': self._get_temperature()
        }
    
    def _get_temperature(self):
        """Get CPU temperature"""
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                return int(f.read()) / 1000.0
        except:
            return None
```

## Audio Configuration

### ALSA Audio Setup
```bash
# Configure audio output for Pi Terminal speakers
sudo nano /etc/asound.conf

# Add configuration:
pcm.!default {
    type hw
    card 0
    device 0
}
ctl.!default {
    type hw
    card 0
}

# Test audio
speaker-test -c2 -t sine -f 440
aplay /usr/share/sounds/alsa/Front_Left.wav
```

### Audio Volume Control
```python
# src/hardware/audio_control.py
import subprocess
import logging

class AudioControl:
    """Manage audio output on Raspberry Pi"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.current_volume = 50
    
    def set_volume(self, volume: int):
        """Set system volume (0-100)"""
        volume = max(0, min(100, volume))
        
        try:
            # Use amixer to control volume
            subprocess.run([
                'amixer', 'sset', 'PCM', f'{volume}%'
            ], check=True, capture_output=True)
            
            self.current_volume = volume
            self.logger.info(f"Volume set to {volume}%")
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to set volume: {e}")
    
    def mute(self):
        """Mute audio output"""
        try:
            subprocess.run([
                'amixer', 'sset', 'PCM', 'mute'
            ], check=True)
        except subprocess.CalledProcessError:
            pass
    
    def unmute(self):
        """Unmute audio output"""
        try:
            subprocess.run([
                'amixer', 'sset', 'PCM', 'unmute'
            ], check=True)
        except subprocess.CalledProcessError:
            pass
```

## Network Configuration

### WiFi Setup for Weather Data
```bash
# Configure WiFi for weather channel
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Add network:
network={
    ssid="YourNetworkName"
    psk="YourPassword"
    key_mgmt=WPA-PSK
}

# Restart networking
sudo systemctl restart dhcpcd
```

### Firewall Configuration
```bash
# Basic firewall setup
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (if needed)
sudo ufw allow ssh

# Allow web traffic for weather channel
sudo ufw allow 80
sudo ufw allow 443
```

## Backup & Recovery

### System Backup Script
```bash
#!/bin/bash
# scripts/backup_pi.sh - Backup Pi configuration

BACKUP_DIR="/media/usb/backups"
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/pi_backup_$DATE.tar.gz"

echo "🔄 Creating system backup..."

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Backup system configuration and application
tar -czf "$BACKUP_FILE" \
    --exclude='/media/usb/tv_content' \
    --exclude='/tmp' \
    --exclude='/var/cache' \
    /opt/90s-crt-tv \
    /home/pi/.bashrc \
    /etc/systemd/system/90s-crt-tv.service \
    /boot/config.txt \
    /etc/asound.conf

echo "✅ Backup created: $BACKUP_FILE"

# Keep only last 5 backups
ls -t "$BACKUP_DIR"/pi_backup_*.tar.gz | tail -n +6 | xargs -r rm

echo "🧹 Old backups cleaned up"
```

### Recovery Procedure
```bash
# Restore from backup
tar -xzf /media/usb/backups/pi_backup_YYYYMMDD_HHMMSS.tar.gz -C /

# Reload systemd
sudo systemctl daemon-reload
sudo systemctl enable 90s-crt-tv.service

# Reboot to apply changes
sudo reboot
```

## Monitoring & Logging

### Log Configuration
```python
# src/utils/pi_logging.py
import logging
import logging.handlers
from pathlib import Path

def setup_pi_logging(log_dir: Path):
    """Configure logging for Pi deployment"""
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    simple_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        log_dir / '90s-tv.log',
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(detailed_formatter)
    root_logger.addHandler(file_handler)
    
    # Console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(simple_formatter)
    console_handler.setLevel(logging.WARNING)  # Only warnings/errors to console
    root_logger.addHandler(console_handler)
    
    # System journal handler (systemd)
    try:
        from systemd.journal import JournalHandler
        journal_handler = JournalHandler()
        journal_handler.setFormatter(simple_formatter)
        root_logger.addHandler(journal_handler)
    except ImportError:
        pass  # systemd not available
```

### Health Monitoring
```python
# src/monitoring/health_monitor.py
import time
import psutil
import logging
from threading import Thread

class HealthMonitor:
    """Monitor system health and performance"""
    
    def __init__(self, tv_controller):
        self.tv_controller = tv_controller
        self.logger = logging.getLogger(__name__)
        self.running = False
        
    def start(self):
        """Start health monitoring thread"""
        self.running = True
        self.monitor_thread = Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        
    def stop(self):
        """Stop health monitoring"""
        self.running = False
        
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                # Check system resources
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                # Log critical conditions
                if cpu_percent > 90:
                    self.logger.warning(f"High CPU usage: {cpu_percent:.1f}%")
                    
                if memory.percent > 90:
                    self.logger.warning(f"High memory usage: {memory.percent:.1f}%")
                    # Signal TV controller to free memory
                    self.tv_controller.optimize_memory()
                
                # Check temperature
                temp = self._get_temperature()
                if temp and temp > 75:
                    self.logger.warning(f"High temperature: {temp:.1f}°C")
                    # Could reduce video quality or frame rate
                    
                # Sleep between checks
                time.sleep(30)
                
            except Exception as e:
                self.logger.error(f"Health monitor error: {e}")
                time.sleep(60)  # Wait longer on error
    
    def _get_temperature(self):
        """Get CPU temperature"""
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                return int(f.read()) / 1000.0
        except:
            return None
```

## Troubleshooting Guide

### Common Issues

#### Video Playback Issues
```bash
# Check VLC installation
vlc --version
python3 -c "import vlc; print('VLC Python bindings OK')"

# Test hardware acceleration
vlc --intf dummy --play-and-exit /path/to/test/video.mp4

# Check GPU memory
vcgencmd get_mem gpu

# Monitor GPU usage
sudo rpi-imager
```

#### Audio Problems
```bash
# List audio devices
aplay -l

# Test audio output
speaker-test -c2 -t sine -f 440

# Check ALSA configuration
cat /proc/asound/cards
```

#### High CPU/Memory Usage
```bash
# Monitor processes
htop

# Check specific to our app
sudo systemctl status 90s-crt-tv.service
sudo journalctl -u 90s-crt-tv.service --since "1 hour ago"

# Memory usage breakdown
free -h
cat /proc/meminfo
```

#### IR Remote Not Working
```bash
# Test IR receiver
sudo systemctl status lircd

# Test raw IR signals
sudo mode2 -d /dev/lirc0

# List available remotes
irw

# Test specific buttons
echo "KEY_1" | irsend SEND_ONCE your_remote_name
```

### Performance Optimization Checklist
- [ ] GPU memory set to 128MB or higher
- [ ] Hardware video acceleration enabled
- [ ] USB 3.0 SSD for media storage
- [ ] Proper cooling (heat sink + fan)
- [ ] Background services minimized
- [ ] Log rotation configured
- [ ] Memory monitoring active
- [ ] Temperature monitoring enabled

### Emergency Recovery
```bash
# If system becomes unresponsive
# Boot into recovery mode and:

# Disable auto-start
sudo systemctl disable 90s-crt-tv.service

# Check logs for issues
sudo journalctl -u 90s-crt-tv.service -n 100

# Reset to safe configuration
sudo cp /boot/config.txt.backup /boot/config.txt
sudo reboot
```

---
*Complete Pi deployment guide ensures stable, optimized operation of 90s TV experience*