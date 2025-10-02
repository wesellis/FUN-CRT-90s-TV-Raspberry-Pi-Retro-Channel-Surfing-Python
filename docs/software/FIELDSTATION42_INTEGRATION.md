# FieldStation42 Integration & Setup Guide

## Overview
This project leverages Shane Mason's proven FieldStation42 software platform with custom extensions for Weather Channel and Gaming integration. FieldStation42 provides the core TV simulation functionality while we add specialized channels.

## FieldStation42 Core Platform

### **Source Project Information**
- **Repository**: https://github.com/shane-mason/FieldStation42
- **License**: Mozilla Public License 2.0
- **Community**: 600+ GitHub stars, active development
- **Documentation**: Comprehensive wiki and examples
- **Creator**: Shane Mason (wrongdog reckons)

### **Key Features We'll Use**
- **Multi-channel simulation** with continuous background playback
- **Realistic scheduling** based on time of day and content type
- **Commercial integration** with automatic break insertion
- **Station bumpers** and network identification
- **Content cataloging** system for metadata management
- **Flexible configuration** via JSON files

### **What FieldStation42 Handles For Us**
- ✅ Channel 1: TV Guide (built-in guide channel)
- ✅ Channels 2-7: Video content with scheduling and commercials
- ✅ Content organization and cataloging
- ✅ Realistic TV scheduling algorithms
- ✅ Commercial break insertion
- ✅ Station bumpers and IDs
- ✅ Background continuous playback
- ✅ Channel switching logic

### **What We'll Add**
- 🔄 Channel 8: Weather Star 4000+ integration
- 🔄 Channel 9: Gaming/EmulationStation integration
- 🔄 Cable box hardware control (LED display, keypad)
- 🔄 CRT TV output optimization

## Installation & Basic Setup

### **System Requirements**
- **Raspberry Pi 5** (8GB recommended)
- **Raspberry Pi OS** (64-bit, desktop or lite)
- **Python 3.9+** with pip
- **MPV media player** for video playback
- **1TB+ USB SSD** for content storage

### **FieldStation42 Installation**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv python3-tk git mpv

# Clone FieldStation42
cd /opt
sudo git clone https://github.com/shane-mason/FieldStation42.git
sudo chown -R pi:pi FieldStation42
cd FieldStation42

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### **Additional Dependencies for Our Extensions**
```bash
# For cable box hardware
pip install tm1637 adafruit-circuitpython-matrixkeypad

# For weather channel integration  
sudo apt install nodejs npm chromium-browser

# For gaming integration
sudo apt install emulationstation retroarch
```

## FieldStation42 Configuration

### **Content Directory Structure**
```
/opt/FieldStation42/
├── catalog/
│   ├── sitcoms/           # Channel 2 content
│   │   ├── seinfeld/
│   │   ├── friends/
│   │   └── commercials/
│   ├── cartoons/          # Channel 3 content  
│   │   ├── animaniacs/
│   │   ├── ducktales/
│   │   └── commercials/
│   ├── nicktoons/         # Channel 4 content
│   ├── anime/             # Channel 5 content
│   ├── comedy/            # Channel 6 content
│   └── mtv/               # Channel 7 content
├── confs/
│   ├── 90s_cable_setup.json
│   └── channel_configs/
└── runtime/
    ├── schedules/
    └── catalogs/
```

### **Channel Configuration Example**
```json
{
  "station_conf": {
    "network_name": "Sitcoms",
    "channel_number": 2,
    "content_dir": "catalog/sitcoms",
    "commercial_dir": "catalog/sitcoms/commercials", 
    "bump_dir": "catalog/sitcoms/bumpers",
    "catalog_path": "runtime/catalogs/sitcoms.bin",
    "schedule_path": "runtime/schedules/sitcoms_schedule.bin",
    "runtime_dir": "runtime/sitcoms",
    "network_type": "standard",
    "schedule_increment": 30,
    "break_strategy": "standard",
    "commercial_free": false,
    "schedule": {
      "6": {"tags": "morning_sitcoms"},
      "7": {"tags": "morning_sitcoms"}, 
      "8": {"tags": "classic_sitcoms"},
      "9": {"tags": "classic_sitcoms"},
      "10": {"tags": "workplace_comedy"},
      "11": {"tags": "workplace_comedy"},
      "12": {"tags": "lunch_laughs"},
      "13": {"tags": "lunch_laughs"},
      "14": {"tags": "afternoon_reruns"},
      "15": {"tags": "afternoon_reruns"},
      "16": {"tags": "after_school"},
      "17": {"tags": "after_school"},
      "18": {"tags": "dinner_time"},
      "19": {"tags": "prime_time"},
      "20": {"tags": "prime_time"},
      "21": {"tags": "prime_time"},
      "22": {"tags": "late_night"},
      "23": {"tags": "late_night"}
    }
  }
}
```

### **Building Catalogs and Schedules**
```bash
# Navigate to FieldStation42 directory
cd /opt/FieldStation42
source env/bin/activate

# Build content catalogs (run after adding new content)
python3 station_42.py --build_catalog --config confs/90s_cable_setup.json

# Generate weekly schedules
python3 station_42.py --build_schedule --config confs/90s_cable_setup.json

# Test the configuration
python3 station_42.py --show_schedule --config confs/90s_cable_setup.json
```

## Custom Channel Extensions

### **Channel 8: Weather Star 4000+ Integration**

#### **Weather App Setup**
```bash
# Install weather application
cd /opt
git clone https://github.com/netbymatt/ws4kp.git
cd ws4kp

# Install dependencies
npm install
npm run build

# Configure for local deployment
cp config.sample.json config.json
# Edit config.json with your location
```

#### **Weather Channel Handler**
```python
# Custom extension: weather_channel.py
import subprocess
import time
import logging

class WeatherChannelHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.weather_process = None
        
    def launch_weather_channel(self):
        """Launch Weather Star 4000+ in fullscreen"""
        try:
            # Stop FieldStation42 playback
            self.pause_fieldstation42()
            
            # Launch weather app in kiosk mode
            self.weather_process = subprocess.Popen([
                'chromium-browser',
                '--kiosk',
                '--autoplay-policy=no-user-gesture-required',
                'http://localhost:3000'
            ])
            
            self.logger.info("Weather channel launched")
            
        except Exception as e:
            self.logger.error(f"Failed to launch weather channel: {e}")
    
    def exit_weather_channel(self):
        """Exit weather and return to FieldStation42"""
        if self.weather_process:
            self.weather_process.terminate()
            self.weather_process = None
            
        # Resume FieldStation42
        self.resume_fieldstation42()
        self.logger.info("Returned to TV from weather channel")
```

### **Channel 9: Gaming Integration**

#### **EmulationStation Setup**
```bash
# Install RetroPie components
sudo apt install emulationstation retroarch

# Create ROM directories
mkdir -p /opt/retropie/roms/{nes,snes,genesis,arcade}

# Configure EmulationStation for our use
mkdir -p ~/.emulationstation
# Copy configuration files for kiosk-style operation
```

#### **Gaming Channel Handler**
```python
# Custom extension: gaming_channel.py
import subprocess
import psutil
import logging

class GamingChannelHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.gaming_process = None
        
    def launch_gaming_channel(self):
        """Launch EmulationStation for retro gaming"""
        try:
            # Free up memory by stopping video streams
            self.stop_fieldstation42_streams()
            
            # Launch EmulationStation
            self.gaming_process = subprocess.Popen([
                'emulationstation',
                '--no-splash',
                '--windowed'
            ])
            
            self.logger.info("Gaming channel launched")
            
            # Monitor for exit
            self.monitor_gaming_exit()
            
        except Exception as e:
            self.logger.error(f"Failed to launch gaming channel: {e}")
    
    def monitor_gaming_exit(self):
        """Monitor EmulationStation and return to TV when done"""
        if self.gaming_process:
            self.gaming_process.wait()
            self.logger.info("Gaming session ended, returning to TV")
            self.restart_fieldstation42()
```

## Cable Box Hardware Integration

### **TM1637 LED Display Control**
```python
# Hardware control: led_display.py
import tm1637
import time

class ChannelDisplay:
    def __init__(self, clk_pin=3, dio_pin=2):
        self.display = tm1637.TM1637(clk=clk_pin, dio=dio_pin)
        self.current_channel = 2
        
    def show_channel(self, channel_number):
        """Display channel number on LED"""
        self.current_channel = channel_number
        
        if channel_number < 10:
            # Show single digit with leading space
            self.display.show(f"  {channel_number} ")
        else:
            # Show two digits
            self.display.show(f" {channel_number} ")
    
    def show_off(self):
        """Turn off display"""
        self.display.show("    ")
    
    def test_display(self):
        """Test all segments"""
        for i in range(1, 10):
            self.show_channel(i)
            time.sleep(0.5)
```

### **Matrix Keypad Input**
```python
# Hardware control: keypad_input.py
import adafruit_matrixkeypad
import digitalio
import board

class CableBoxKeypad:
    def __init__(self):
        # Define keypad layout
        self.keys = [
            [1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9],
            ['*', 0, '#']
        ]
        
        # GPIO pin assignments
        self.cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D11, board.D9)]
        self.rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D19, board.D13, board.D6)]
        
        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(self.rows, self.cols, self.keys)
        
    def get_channel_input(self):
        """Get channel number from keypad"""
        channel_buffer = ""
        
        while True:
            keys = self.keypad.pressed_keys
            if keys:
                key = keys[0]
                
                if key == '#':  # Enter channel
                    if channel_buffer:
                        return int(channel_buffer)
                elif key == '*':  # Clear
                    channel_buffer = ""
                elif isinstance(key, int):
                    channel_buffer += str(key)
                    if len(channel_buffer) >= 2:  # Auto-enter after 2 digits
                        return int(channel_buffer)
```

## Main Integration Controller

### **Master Channel Controller**
```python
# Main integration: channel_controller.py
import logging
from fieldstation42_wrapper import FieldStation42Wrapper
from weather_channel import WeatherChannelHandler
from gaming_channel import GamingChannelHandler
from led_display import ChannelDisplay
from keypad_input import CableBoxKeypad

class MasterChannelController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.fieldstation42 = FieldStation42Wrapper()
        self.weather = WeatherChannelHandler()
        self.gaming = GamingChannelHandler() 
        self.display = ChannelDisplay()
        self.keypad = CableBoxKeypad()
        
        self.current_channel = 2
        
    def start(self):
        """Start the master controller"""
        self.logger.info("Starting 90s Cable TV experience...")
        
        # Start FieldStation42
        self.fieldstation42.start()
        
        # Show initial channel
        self.change_channel(self.current_channel)
        
        # Start input monitoring
        self.monitor_inputs()
        
    def change_channel(self, new_channel):
        """Handle channel changes"""
        if new_channel == self.current_channel:
            return
            
        self.logger.info(f"Changing channel: {self.current_channel} → {new_channel}")
        
        # Update display
        self.display.show_channel(new_channel)
        
        if new_channel in [1, 2, 3, 4, 5, 6, 7]:
            # Regular FieldStation42 channels
            self.fieldstation42.change_channel(new_channel)
            
        elif new_channel == 8:
            # Weather channel
            self.weather.launch_weather_channel()
            
        elif new_channel == 9:
            # Gaming channel
            self.gaming.launch_gaming_channel()
            
        self.current_channel = new_channel
        
    def monitor_inputs(self):
        """Monitor keypad for channel changes"""
        while True:
            try:
                channel = self.keypad.get_channel_input()
                if 1 <= channel <= 9:
                    self.change_channel(channel)
            except Exception as e:
                self.logger.error(f"Input error: {e}")
```

## Deployment Configuration

### **Systemd Service Setup**
```ini
# /etc/systemd/system/90s-cable-tv.service
[Unit]
Description=90s Cable TV Experience
After=network.target graphical-session.target

[Service]
Type=simple
User=pi
Group=pi
WorkingDirectory=/opt/FieldStation42
Environment=DISPLAY=:0
Environment=XDG_RUNTIME_DIR=/run/user/1000
ExecStart=/opt/FieldStation42/env/bin/python /opt/FieldStation42/cable_tv_main.py
Restart=always
RestartSec=10

[Install]
WantedBy=graphical-session.target
```

### **Auto-start Configuration**
```bash
# Enable service
sudo systemctl daemon-reload
sudo systemctl enable 90s-cable-tv.service

# Test service
sudo systemctl start 90s-cable-tv.service
sudo systemctl status 90s-cable-tv.service
```

---
*Integration guide provides roadmap for extending FieldStation42 with Weather and Gaming channels while maintaining core TV simulation functionality*