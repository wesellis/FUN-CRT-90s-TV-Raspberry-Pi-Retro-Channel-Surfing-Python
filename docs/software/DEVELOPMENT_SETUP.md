# Software Development Setup & Configuration

## Development Environment Setup

### Prerequisites
- **Python 3.9+** with pip package manager
- **Git** for version control
- **VLC Media Player** for video playback
- **FFmpeg** for video processing
- **Code editor** (VS Code, PyCharm, etc.)

### Python Environment Configuration

#### Virtual Environment Setup
```bash
# Create isolated Python environment
cd C:\Users\wesle\Dropbox\GITHUB\FUN-CRT-90s-TV
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Linux/Pi:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Requirements.txt Breakdown
```python
# Core video playback
pygame>=2.5.0          # UI and overlays
python-vlc>=3.0.18121  # Video player integration

# Networking and APIs  
requests>=2.31.0       # Weather data fetching

# Scheduling and timing
schedule>=1.2.0        # Cron-like scheduling

# Raspberry Pi specific (install only on Pi)
RPi.GPIO>=0.7.1        # GPIO control for IR receiver
python-lirc>=1.2.3     # IR remote handling

# Image and video processing
opencv-python>=4.8.0   # Video analysis and effects
numpy>=1.24.0          # Numerical processing
Pillow>=10.0.0         # Image processing

# Development tools
pytest>=7.4.0          # Unit testing
black>=23.7.0          # Code formatting
flake8>=6.0.0          # Code linting
```

### Cross-Platform Configuration

#### Platform Detection Module
```python
# src/utils/platform_config.py
import platform
import os
from pathlib import Path

class PlatformConfig:
    def __init__(self):
        self.system = platform.system()
        self.is_windows = self.system == "Windows"
        self.is_linux = self.system == "Linux"
        self.is_pi = self.is_linux and self.detect_raspberry_pi()
    
    def detect_raspberry_pi(self):
        """Detect if running on Raspberry Pi"""
        try:
            with open('/proc/cpuinfo', 'r') as f:
                return 'BCM' in f.read()
        except:
            return False
    
    @property
    def media_root(self):
        if self.is_windows:
            return Path("C:/Users/wesle/Videos/TV_Content")
        else:
            return Path("/media/usb/tv_content")
    
    @property
    def vlc_path(self):
        if self.is_windows:
            return "C:/Program Files/VideoLAN/VLC/vlc.exe"
        else:
            return "/usr/bin/vlc"
    
    @property
    def config_dir(self):
        if self.is_windows:
            return Path.home() / "AppData/Local/90s-CRT-TV"
        else:
            return Path.home() / ".config/90s-crt-tv"
```

#### Environment Variables
```python
# .env configuration file
# Development settings
DEBUG=True
LOG_LEVEL=DEBUG
MEDIA_ROOT=C:\Users\wesle\Videos\TV_Content

# Production settings (Pi deployment)
# DEBUG=False
# LOG_LEVEL=INFO
# MEDIA_ROOT=/media/usb/tv_content

# Weather channel settings
WEATHER_API_KEY=your_api_key_here
WEATHER_LOCATION=Charlottesville,VA

# Hardware settings
IR_RECEIVER_PIN=18
CHANNEL_OVERLAY_DURATION=3
CRT_EFFECTS_ENABLED=True
```

### Code Structure & Patterns

#### Main Application Architecture
```python
# src/main.py - Application entry point
#!/usr/bin/env python3
"""
90s CRT TV - Main Application
"""
import sys
import logging
from pathlib import Path

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent))

from core.tv_controller import TVController
from utils.platform_config import PlatformConfig
from utils.logger import setup_logging

def main():
    """Main application entry point"""
    # Setup logging
    config = PlatformConfig()
    setup_logging(config.config_dir / "logs")
    
    logger = logging.getLogger(__name__)
    logger.info("🖥️ 90s CRT TV Starting...")
    
    try:
        # Initialize and start TV
        tv = TVController(config)
        tv.power_on()
        tv.run()
        
    except KeyboardInterrupt:
        logger.info("📺 TV Powered Off - User interrupt")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### Core TV Controller Class
```python
# src/core/tv_controller.py
import logging
import threading
import time
from typing import Dict, Optional

from .channel_manager import ChannelManager
from .input_handler import InputHandler
from .overlay_manager import OverlayManager
from ..utils.config_loader import ConfigLoader

class TVController:
    """Main TV system coordinator"""
    
    def __init__(self, platform_config):
        self.config = platform_config
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.settings = ConfigLoader(self.config.config_dir).load()
        
        # Initialize subsystems
        self.channel_manager = ChannelManager(self.config, self.settings)
        self.input_handler = InputHandler(self.config)
        self.overlay_manager = OverlayManager(self.config)
        
        # State
        self.current_channel = 2  # Default to sitcoms
        self.is_running = False
        self.last_interaction = time.time()
        
    def power_on(self):
        """Initialize and start all TV subsystems"""
        self.logger.info("📺 Powering on TV...")
        
        # Start background systems
        self.channel_manager.start()
        self.input_handler.start(self.handle_input)
        
        # Load initial channels
        self.channel_manager.preload_channels([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        # Switch to default channel
        self.change_channel(self.current_channel)
        
        self.is_running = True
        self.logger.info("✅ TV ready - Channel surfing enabled!")
    
    def handle_input(self, input_event):
        """Process user input (remote, keyboard, etc.)"""
        self.last_interaction = time.time()
        
        if input_event.type == "channel_number":
            self.change_channel(input_event.value)
        elif input_event.type == "channel_up":
            self.channel_up()
        elif input_event.type == "channel_down":
            self.channel_down()
        elif input_event.type == "power":
            self.power_off()
    
    def change_channel(self, new_channel: int):
        """Switch to specified channel"""
        if new_channel == self.current_channel:
            return
            
        self.logger.info(f"📺 Changing channel: {self.current_channel} → {new_channel}")
        
        # Show channel overlay
        channel_info = self.channel_manager.get_channel_info(new_channel)
        self.overlay_manager.show_channel_overlay(new_channel, channel_info.name)
        
        # Switch video/app
        success = self.channel_manager.switch_to_channel(new_channel)
        if success:
            self.current_channel = new_channel
        else:
            self.logger.warning(f"❌ Failed to switch to channel {new_channel}")
    
    def run(self):
        """Main application loop"""
        try:
            while self.is_running:
                # Update systems
                self.channel_manager.update()
                self.overlay_manager.update()
                
                # Handle any scheduled events
                self._handle_scheduled_events()
                
                # Sleep to prevent high CPU usage
                time.sleep(0.1)
                
        except Exception as e:
            self.logger.error(f"💥 Main loop error: {e}", exc_info=True)
        finally:
            self.power_off()
    
    def power_off(self):
        """Shutdown TV systems"""
        self.logger.info("📺 Powering off TV...")
        self.is_running = False
        
        # Cleanup subsystems
        if hasattr(self, 'channel_manager'):
            self.channel_manager.stop()
        if hasattr(self, 'input_handler'):
            self.input_handler.stop()
        
        self.logger.info("✅ TV powered off cleanly")
```

### Development Tools & Scripts

#### Code Quality Tools
```bash
# Format code with Black
black src/ tests/

# Lint code with flake8
flake8 src/ tests/ --max-line-length=88

# Run type checking
mypy src/

# Run unit tests
pytest tests/ -v
```

#### Development Scripts
```python
# scripts/dev_setup.py - Development environment setup
#!/usr/bin/env python3
"""Setup development environment"""

import subprocess
import sys
from pathlib import Path

def install_dependencies():
    """Install all required packages"""
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
def setup_vlc():
    """Verify VLC installation"""
    try:
        import vlc
        print("✅ VLC Python bindings installed")
    except ImportError:
        print("❌ VLC Python bindings missing")
        print("Install VLC media player first")

def create_test_content():
    """Create sample content for testing"""
    test_dir = Path("media/test_content")
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Create placeholder files
    for channel in range(2, 10):
        channel_dir = test_dir / f"channel_{channel:02d}"
        channel_dir.mkdir(exist_ok=True)
        
        # Create test video placeholder
        test_file = channel_dir / "test_episode.txt"
        test_file.write_text("Test content placeholder")

if __name__ == "__main__":
    print("🚀 Setting up 90s CRT TV development environment...")
    install_dependencies()
    setup_vlc()
    create_test_content()
    print("✅ Development environment ready!")
```

### Testing Framework

#### Unit Test Structure
```python
# tests/test_channel_manager.py
import unittest
from unittest.mock import Mock, patch
import sys
from pathlib import Path

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from core.channel_manager import ChannelManager
from utils.platform_config import PlatformConfig

class TestChannelManager(unittest.TestCase):
    def setUp(self):
        """Setup test environment"""
        self.config = Mock(spec=PlatformConfig)
        self.config.media_root = Path("tests/fixtures/media")
        self.config.is_pi = False
        
        self.channel_manager = ChannelManager(self.config, {})
    
    def test_channel_switching(self):
        """Test basic channel switching functionality"""
        # Test switching to valid channel
        result = self.channel_manager.switch_to_channel(2)
        self.assertTrue(result)
        
        # Test switching to invalid channel
        result = self.channel_manager.switch_to_channel(99)
        self.assertFalse(result)
    
    def test_program_scheduling(self):
        """Test time-based program calculation"""
        from datetime import datetime, time
        
        # Mock current time to 3:00 PM
        test_time = datetime.combine(datetime.today(), time(15, 0))
        
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = test_time
            
            program = self.channel_manager.get_current_program(2, test_time)
            self.assertIsNotNone(program)
            self.assertIn('file_path', program)
            self.assertIn('seek_position', program)

if __name__ == "__main__":
    unittest.main()
```

#### Integration Test Setup
```python
# tests/test_integration.py
import unittest
import tempfile
import shutil
from pathlib import Path

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        """Create temporary media structure for testing"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.create_test_media_structure()
    
    def tearDown(self):
        """Cleanup test files"""
        shutil.rmtree(self.temp_dir)
    
    def create_test_media_structure(self):
        """Create realistic test media directory"""
        # Create channel directories
        for channel in range(2, 10):
            channel_dir = self.temp_dir / f"channel_{channel:02d}_test"
            shows_dir = channel_dir / "shows"
            shows_dir.mkdir(parents=True)
            
            # Create test video files
            test_show_dir = shows_dir / "test_show"
            test_show_dir.mkdir()
            
            for episode in range(1, 4):
                episode_file = test_show_dir / f"test_show_s01e{episode:02d}.mp4"
                episode_file.write_text("test video content")
    
    def test_full_tv_startup(self):
        """Test complete TV startup sequence"""
        # This would test the full integration
        # but requires actual video files and VLC
        pass
```

### Configuration Management

#### Settings Configuration
```json
{
  "channels": {
    "default_channel": 2,
    "preload_adjacent": true,
    "switch_timeout": 2.0
  },
  "display": {
    "resolution": "960x720",
    "crt_effects": true,
    "overlay_duration": 3.0,
    "overlay_style": "green_90s"
  },
  "audio": {
    "normalize_volume": true,
    "fade_duration": 0.5,
    "commercial_volume_boost": 1.1
  },
  "input": {
    "ir_receiver_pin": 18,
    "debounce_time": 0.3,
    "keyboard_enabled": true
  },
  "weather": {
    "api_key": "",
    "location": "Charlottesville,VA",
    "update_interval": 600,
    "smooth_jazz": true
  },
  "gaming": {
    "emulationstation_path": "/opt/retropie/bin/emulationstation",
    "preload_gaming": true,
    "controller_priority": "usb"
  }
}
```

### Deployment Configuration

#### Pi Deployment Script
```bash
#!/bin/bash
# scripts/deploy_to_pi.sh - Deploy to Raspberry Pi

PI_HOST="raspberrypi.local"
PI_USER="pi"
PROJECT_DIR="/home/pi/90s-crt-tv"

echo "🚀 Deploying 90s CRT TV to Raspberry Pi..."

# Copy source code
rsync -av --exclude='media/' --exclude='__pycache__/' \
    --exclude='.git/' --exclude='venv/' \
    ./ ${PI_USER}@${PI_HOST}:${PROJECT_DIR}/

# Install dependencies on Pi
ssh ${PI_USER}@${PI_HOST} "cd ${PROJECT_DIR} && \
    python3 -m venv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt"

# Setup systemd service
ssh ${PI_USER}@${PI_HOST} "sudo cp ${PROJECT_DIR}/scripts/90s-tv.service /etc/systemd/system/ && \
    sudo systemctl daemon-reload && \
    sudo systemctl enable 90s-tv.service"

echo "✅ Deployment complete! Reboot Pi to auto-start."
```

---
*Comprehensive development setup ensures smooth progression from PC development to Pi deployment*