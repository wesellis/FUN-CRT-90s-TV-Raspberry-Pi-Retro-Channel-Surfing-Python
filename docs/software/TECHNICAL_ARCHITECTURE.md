# Technical Architecture & Software Design

## System Overview
The 90s CRT TV system runs multiple background video streams and switches between them based on user input and real-time scheduling, creating an authentic TV channel surfing experience.

## Core Architecture

### Platform Strategy
- **Development Platform**: Windows PC (faster iteration)
- **Target Platform**: Raspberry Pi 5 (final deployment)
- **Cross-Platform Libraries**: VLC, Pygame, Python standard library

### Main Components
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   TV Controller │───▶│ Channel Manager │───▶│ Video Players   │
│   (main.py)     │    │                 │    │ (VLC instances) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Input Handler  │    │   Scheduler     │    │    Overlay      │
│  (IR/Keyboard)  │    │   (time calc)   │    │   (channel UI)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Performance Requirements

### Raspberry Pi 5 Capabilities
- **CPU**: Quad-core ARM Cortex-A76 @ 2.4GHz
- **RAM**: 8GB (6GB usable after OS)
- **GPU**: VideoCore VII with hardware H.264/H.265 decoding
- **Storage**: USB 3.0 SSD for fast video access

### Resource Allocation
```python
# Per 720p video stream (estimated)
RAM_per_stream = 100  # MB
CPU_per_stream = 5    # % (with hardware decoding)
Storage_bandwidth = 50  # MB/s per stream

# 8 channels maximum
Total_RAM = 8 * 100 = 800  # MB (well within 6GB available)
Total_CPU = 8 * 5 = 40     # % (manageable load)
Total_Storage = 8 * 50 = 400  # MB/s (within USB 3.0 limits)
```

## Channel Management System

### Background Stream Strategy
```python
class ChannelManager:
    def __init__(self):
        self.active_channels = {}  # Currently loaded streams
        self.current_channel = 2   # Default to sitcoms
        
    def preload_channels(self, channel_list):
        """Load multiple channels in background"""
        for channel in channel_list:
            player = vlc.MediaPlayer()
            # Load current program for this channel
            current_program = self.get_current_program(channel)
            player.set_media(current_program.file_path)
            player.play()
            player.set_time(current_program.seek_position)
            player.pause()  # Keep loaded but paused
            
            self.active_channels[channel] = player
```

### Smart Loading Strategy
- **Active**: Current channel + adjacent channels (instant switching)
- **Lazy**: Distant channels loaded on-demand (~1-2 second delay)
- **Memory Management**: Unload unused channels after timeout

## Scheduling System

### Time-Based Programming
```python
class ProgramSchedule:
    def __init__(self):
        self.schedules = self.load_channel_schedules()
    
    def get_current_program(self, channel, current_time):
        """Calculate what should be playing now"""
        schedule = self.schedules[channel]
        
        # Find current time slot
        for time_slot in schedule:
            if self.time_in_range(current_time, time_slot):
                # Calculate position within episode
                elapsed = current_time - time_slot.start_time
                return {
                    'show': time_slot.show,
                    'episode': time_slot.episode,
                    'file_path': time_slot.file_path,
                    'seek_position': elapsed.total_seconds()
                }
```

### Commercial Integration
```python
class CommercialManager:
    def should_show_commercial(self, show_progress):
        """Determine if commercial break should occur"""
        # Every ~22 minutes for sitcoms, ~12 minutes for hour shows
        break_points = [660, 1320]  # 11min, 22min in seconds
        return any(abs(show_progress - bp) < 30 for bp in break_points)
    
    def create_commercial_break(self, channel_type):
        """Generate 2-3 commercials + fade transitions"""
        commercials = self.select_random_commercials(channel_type, count=3)
        return self.add_transitions(commercials)
```

## Video Playback Strategy

### VLC Integration
```python
class VideoPlayer:
    def __init__(self):
        self.instance = vlc.Instance([
            '--intf', 'dummy',           # No GUI
            '--no-video-title-show',     # No filename overlay
            '--no-audio-visual',         # No visualizations
            '--video-filter=deinterlace' # Better quality
        ])
        
    def apply_crt_effects(self, player):
        """Add retro CRT styling"""
        # Use VLC's built-in filters or external shaders
        player.video_set_adjust_int(vlc.VideoAdjustOption.Enable, 1)
        player.video_set_adjust_float(vlc.VideoAdjustOption.Contrast, 1.2)
        player.video_set_adjust_float(vlc.VideoAdjustOption.Saturation, 1.1)
```

### Alternative: RetroArch for CRT Shaders
```python
def apply_retroarch_shaders(video_file):
    """Use RetroArch's superior CRT shaders"""
    cmd = [
        'retroarch',
        '-L', 'ffmpeg_libretro.so',
        '--config', 'crt_config.cfg',
        video_file
    ]
    subprocess.run(cmd)
```

## User Interface System

### Channel Overlay
```python
class ChannelOverlay:
    def show_channel_info(self, channel_num, channel_name):
        """Display green 90s-style channel overlay"""
        overlay = pygame.Surface((200, 80))
        overlay.fill((0, 255, 0))  # Green background
        overlay.set_alpha(200)     # Semi-transparent
        
        font = pygame.font.Font('assets/fonts/crt_font.ttf', 24)
        text = font.render(f'CH {channel_num}', True, (0, 0, 0))
        overlay.blit(text, (10, 10))
        
        # Auto-hide after 3 seconds
        threading.Timer(3.0, self.hide_overlay).start()
```

### TV Guide Channel
```python
class TVGuideChannel:
    def generate_guide(self):
        """Create scrolling TV guide display"""
        current_time = datetime.now()
        guide_content = []
        
        for channel in range(2, 10):
            current_show = self.get_current_program(channel, current_time)
            next_show = self.get_next_program(channel, current_time)
            
            guide_content.append({
                'channel': channel,
                'current': current_show,
                'next': f"Next: {next_show.name}",
                'time_remaining': self.calculate_time_left(current_show)
            })
        
        return self.render_scrolling_guide(guide_content)
```

## Input Handling

### IR Remote Integration
```python
class RemoteHandler:
    def __init__(self):
        import lirc
        self.lirc = lirc
        self.remote_map = {
            'KEY_1': 1, 'KEY_2': 2, 'KEY_3': 3,
            'KEY_CHANNELUP': 'channel_up',
            'KEY_CHANNELDOWN': 'channel_down'
        }
    
    def handle_remote_input(self):
        """Process IR remote commands"""
        while True:
            button = self.lirc.nextcode()
            if button:
                action = self.remote_map.get(button[0])
                if action:
                    self.tv_controller.handle_input(action)
```

### Gaming Channel Integration
```python
class GamingChannel:
    def __init__(self):
        self.emulation_process = None
        self.preload_emulationstation()
    
    def preload_emulationstation(self):
        """Start EmulationStation in background"""
        self.emulation_process = subprocess.Popen([
            'emulationstation',
            '--windowed',
            '--hidden'
        ])
    
    def switch_to_gaming(self):
        """Instant switch to game selection"""
        self.hide_video_players()
        self.emulation_process.send_signal(signal.SIGUSR1)  # Show window
```

## Performance Optimizations

### Video File Specifications
- **Format**: MP4 with H.264 encoding
- **Resolution**: 720p maximum (perfect for 8" display)
- **Bitrate**: 1-2 Mbps (keeps files 100-150MB)
- **Audio**: AAC stereo, normalized levels

### Memory Management
```python
class MemoryManager:
    def optimize_streams(self):
        """Manage active video streams"""
        # Keep current + 2 adjacent channels active
        # Unload channels not accessed for 5+ minutes
        # Preload popular channels during low usage
        pass
```

### Storage Optimization
- **SSD Performance**: USB 3.0 for fast seeking
- **File Organization**: Channels in separate directories
- **Caching**: Frequently accessed content in faster storage

## Development Workflow

### PC Development Setup
```python
# Platform detection for cross-compatibility
import platform

if platform.system() == "Windows":
    # PC development paths
    MEDIA_ROOT = "C:/Users/wesle/Videos/TV_Content/"
    VLC_PATH = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    
elif platform.system() == "Linux":
    # Pi deployment paths
    MEDIA_ROOT = "/media/usb/tv_content/"
    VLC_PATH = "/usr/bin/vlc"
```

### Testing Strategy
1. **Unit Tests**: Individual channel/scheduling functions
2. **Integration Tests**: Multi-channel switching
3. **Performance Tests**: Resource usage monitoring
4. **User Tests**: Channel surfing experience

---
*Software architecture designed for smooth 90s TV nostalgia experience*
