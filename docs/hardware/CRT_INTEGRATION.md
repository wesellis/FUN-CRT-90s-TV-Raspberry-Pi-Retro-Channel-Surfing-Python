# CRT Television Integration Guide

## Overview
Connecting the Raspberry Pi 5 to authentic CRT televisions is essential for the genuine 90s cable TV experience. This guide covers video signal conversion, configuration, and optimization for period-correct displays.

## Video Signal Conversion Options

### **Option 1: HDMI to Component Video (Recommended)**

#### **Simple Converters ($15-25)**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| Generic HDMI to Component | Basic converter with component + audio out | Amazon/eBay | $15 |
| Component cables | Red/Blue/Green video + Red/White audio | Amazon | $8 |
| Power adapter | Usually USB powered or wall adapter | Included | $0 |

**Total Budget Option: ~$23**

#### **Quality Converters ($30-50)**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| Portta HDMI to Component | Well-reviewed brand with better scaling | Amazon | $35 |
| OREI HDMI to Component | Professional grade converter | Amazon | $40 |
| High-quality component cables | Gold-plated connectors, better shielding | Amazon | $10 |

**Total Quality Option: ~$45**

#### **Benefits of Component Video**
- **Excellent image quality** - Progressive scan 480p/720p
- **Better than composite** - Sharper image, superior colors
- **Wide compatibility** - Most CRTs from late 90s+ have component inputs
- **Professional appearance** - Red/Blue/Green jacks look authentic

### **Option 2: HDMI to Composite Video (Alternative)**

#### **Composite Converters ($10-15)**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| HDMI to RCA Composite | Yellow video + Red/White audio | Amazon | $12 |
| RCA composite cables | Standard yellow/red/white cables | Amazon | $5 |

**Total Composite Option: ~$17**

#### **Benefits of Composite Video**
- **Universal compatibility** - Works with ANY CRT TV from 80s+
- **Lower cost** - Cheapest conversion option
- **Simple connection** - Single yellow video cable
- **Authentic SD quality** - Matches 90s cable TV resolution

#### **Drawbacks of Composite**
- **Lower image quality** - 480i interlaced, softer image
- **Color bleeding** - Less sharp than component
- **Acceptable for nostalgia** - Still authentic 90s experience

## Pi 5 Video Configuration

### **Component Video Settings (config.txt)**
```bash
# Raspberry Pi 5 configuration for component output
# Edit /boot/config.txt

# Component video optimization
hdmi_group=1
hdmi_mode=4        # 720x480 60Hz (480p progressive)
# Alternative high-res mode:
# hdmi_mode=5      # 1920x1080 60Hz (1080i interlaced)

# Force 4:3 aspect ratio for authentic 90s look
hdmi_cvt=720 480 60 1 0 0 0

# Boost HDMI signal strength for converter compatibility
config_hdmi_boost=4
hdmi_drive=2

# Disable overscan for clean edges
disable_overscan=1

# Force HDMI mode (don't auto-detect)
hdmi_force_hotplug=1
```

### **Composite Video Settings (config.txt)**
```bash
# Raspberry Pi 5 configuration for composite output
# Edit /boot/config.txt

# Standard definition composite
hdmi_group=2
hdmi_mode=87
hdmi_cvt=640 480 60 1 0 0 0  # 4:3 SD resolution

# Signal boost for converter
config_hdmi_boost=7
hdmi_drive=1

# Overscan for CRT TVs (may need adjustment)
overscan_left=16
overscan_right=16
overscan_top=16
overscan_bottom=16
```

### **Alternative Resolutions for Different CRTs**
```bash
# For older CRTs that prefer specific modes:

# 480i interlaced (most compatible)
hdmi_cvt=720 480 60 1 0 0 0

# 240p for retro gaming feel (if supported)
hdmi_cvt=320 240 60 1 0 0 0

# European PAL standard
hdmi_cvt=720 576 50 1 0 0 0
```

## Physical Connection Setup

### **Component Video Connection**
```
Raspberry Pi 5 → HDMI to Component Converter → CRT Television

Pi 5 Connections:
├── HDMI Output → Converter HDMI Input
└── USB-C Power → Pi Power Supply

Converter Connections:
├── Component Video Out → TV Component Inputs
│   ├── Y (Green) → Green jack on TV
│   ├── Pb (Blue) → Blue jack on TV  
│   └── Pr (Red) → Red jack on TV
├── Audio Out → TV Audio Inputs
│   ├── Left (White) → White jack on TV
│   └── Right (Red) → Red jack on TV
└── Power → USB or wall adapter
```

### **Composite Video Connection**
```
Raspberry Pi 5 → HDMI to Composite Converter → CRT Television

Pi 5 Connections:
├── HDMI Output → Converter HDMI Input
└── USB-C Power → Pi Power Supply

Converter Connections:
├── Composite Video (Yellow) → TV Video Input
└── Stereo Audio → TV Audio Inputs
    ├── Left (White) → White jack on TV
    └── Right (Red) → Red jack on TV
```

## CRT Television Compatibility

### **CRT TV Input Types by Era**

#### **Late 90s - 2000s CRTs (Best Compatibility)**
- **Component inputs** (Red/Blue/Green) - Recommended
- **S-Video** (if converter supports it)
- **Composite** (Yellow/Red/White) - Backup option
- **RF/Antenna** (Channel 3/4) - Last resort

#### **Early-Mid 90s CRTs (Good Compatibility)**
- **Composite** (Yellow/Red/White) - Primary option
- **S-Video** (higher-end models)
- **RF/Antenna** (Channel 3/4) - Always available

#### **80s - Early 90s CRTs (Limited Compatibility)**
- **RF/Antenna** (Channel 3/4) - Only option
- **Requires RF modulator** - HDMI → RF converter (~$25)

### **Identifying Your CRT's Inputs**
```
Look for these connectors on your CRT TV:

Component Video:
├── 3 RCA jacks (Red/Blue/Green) labeled Y/Pb/Pr or Y/Cb/Cr
└── Usually grouped together, often on side or back

Composite Video:
├── 3 RCA jacks (Yellow/Red/White)
├── Yellow = Video, Red/White = Audio
└── Most common on 90s TVs

S-Video:
├── Round 4-pin connector
├── Better quality than composite
└── Less common than composite

RF/Antenna:
├── Coaxial screw connector or push-on F-connector
├── Usually labeled "ANT IN" or "VHF/UHF"
└── Available on all CRT TVs
```

## Testing and Optimization

### **Initial Setup Process**
1. **Test converter with modern TV first**
   - Verify Pi 5 HDMI output works
   - Confirm converter functionality
   - Check cable connections

2. **Connect to CRT television**
   - Power off CRT before connecting
   - Connect all cables securely
   - Power on CRT and select correct input

3. **Adjust Pi 5 settings**
   - Modify config.txt as needed
   - Reboot Pi after changes
   - Test different resolution modes

### **Troubleshooting Common Issues**

#### **No Signal on CRT**
```bash
# Try different HDMI modes in config.txt
hdmi_mode=1    # VGA 640x480 60Hz
hdmi_mode=2    # 480p 720x480 60Hz  
hdmi_mode=4    # 720p 1280x720 60Hz
hdmi_mode=16   # 1080p 1920x1080 60Hz

# Force HDMI output
hdmi_force_hotplug=1
hdmi_drive=2
```

#### **Wrong Aspect Ratio**
```bash
# Force 4:3 aspect ratio
hdmi_cvt=640 480 60 1 0 0 0   # True 4:3
hdmi_cvt=720 480 60 1 0 0 0   # NTSC DTV
hdmi_aspect=1                  # Force 4:3

# Adjust overscan if image is cut off
overscan_left=24
overscan_right=24
overscan_top=24
overscan_bottom=24
```

#### **Poor Image Quality**
```bash
# Increase HDMI signal strength
config_hdmi_boost=7

# Disable dithering
hdmi_enable_dither=0

# Force RGB color space
hdmi_pixel_encoding=0
```

### **FieldStation42 Optimization for CRT**

#### **Video Player Settings**
```python
# FieldStation42 CRT optimization
# Add to station configuration

"video_settings": {
    "deinterlace": true,
    "aspect_ratio": "4:3", 
    "scaling": "nearest",
    "color_space": "bt601"
}
```

#### **Content Preparation for CRT**
- **Use 480p source material** when possible
- **4:3 aspect ratio content** looks best
- **Avoid high-contrast graphics** that may cause flickering
- **Test commercial breaks** for consistent quality

## Recommended Hardware Configurations

### **Budget CRT Setup (~$25)**
```
Components:
- Generic HDMI to Composite converter  $12
- RCA composite cables                 $5
- Any CRT TV with composite inputs     $0-50 (used)

Best for:
- Testing and proof of concept
- Budget builds for friends
- CRTs without component inputs
```

### **Quality CRT Setup (~$45)**
```
Components:
- Portta HDMI to Component converter   $35
- High-quality component cables        $10
- Late 90s+ CRT with component inputs  $25-75 (used)

Best for:
- Primary personal build
- Best possible image quality
- Professional demonstrations
```

### **Premium CRT Setup (~$75)**
```
Components:
- OREI HDMI to Component converter     $40
- Premium gold-plated cables           $15
- High-end CRT TV (Sony, Panasonic)    $50-150 (used)
- RF modulator for antenna input       $20

Best for:
- Ultimate authenticity
- Multiple input options
- Future-proofing
```

## CRT TV Shopping Guide

### **Recommended CRT TV Models**

#### **Excellent Options (Component + Composite)**
- **Sony Trinitron** (KV series) - Excellent picture quality
- **Panasonic Tau** (CT series) - Reliable, good color
- **JVC I'Art** (AV series) - Great for gaming
- **Toshiba CinemaWide** - Good component implementation

#### **Good Options (Composite Only)**
- **Sony Trinitron** (earlier models) - Still excellent picture
- **RCA ColorTrak** - Common and affordable
- **Zenith Space Command** - Reliable construction
- **Magnavox** (any model) - Budget-friendly

#### **What to Look For**
- **Size**: 19-27 inches optimal for cable box setup
- **Inputs**: Component preferred, composite minimum
- **Condition**: Powers on, good picture, working remote
- **Age**: Late 90s - early 2000s for best compatibility

#### **What to Avoid**
- **Very old CRTs** (pre-1990) - Limited input options
- **Projection TVs** - Different technology, compatibility issues
- **Damaged CRTs** - Convergence problems, color issues
- **No remote control** - Difficult to access inputs

## Benefits of Real CRT vs LCD Emulation

### **Authentic Visual Experience**
- **Natural scanlines** - Real phosphor pattern, not simulated
- **Phosphor glow** - Genuine light emission characteristics  
- **Color temperature** - Warm, period-correct color reproduction
- **Motion handling** - No LCD motion blur or artifacts

### **Technical Advantages**
- **Zero input lag** - CRTs have virtually no processing delay
- **Perfect black levels** - True black when phosphors are off
- **Viewing angles** - Consistent image from any angle
- **Refresh characteristics** - Natural flicker matches era content

### **Nostalgic Authenticity**
- **Period-correct technology** - Actually what people used in 90s
- **Physical presence** - Weight, size, and form factor of real TV
- **Audio quality** - CRT speakers often superior to modern LCD TV speakers
- **Complete experience** - Matches the cable box aesthetic perfectly

---
*CRT integration provides the ultimate authentic 90s TV experience, with multiple quality and budget options to suit any build*