# FieldStation42 Cable Box Hardware Platform

## Overview
This project now uses Shane Mason's proven FieldStation42 software with his custom 3D printed cable box hardware. This approach provides a professional, authentic cable TV experience at a fraction of the cost of custom hardware builds.

## Source Projects

### **FieldStation42 Software**
- **Repository**: https://github.com/shane-mason/FieldStation42
- **Description**: Broadcast & Cable TV simulator with authentic scheduling
- **License**: Mozilla Public License 2.0
- **Community**: Active development with 600+ stars, comprehensive wiki

### **Cable Box Hardware**
- **Repository**: https://github.com/shane-mason/cable-box
- **Description**: 3D printable cable box replica housing for Raspberry Pi 5
- **Components**: LED display, matrix keypad, authentic form factor
- **Integration**: Designed specifically for FieldStation42

## Complete Hardware Bill of Materials

### **Core Components**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| Raspberry Pi 5 (8GB) | Main computing platform | [Rpilocator](https://rpilocator.com/) | $80 |
| MicroSD Card (64GB) | Operating system storage | Amazon/Local | $15 |
| USB 3.0 SSD (1TB) | Media content storage | Amazon | $90 |
| Official Pi 5 Power Supply | 27W USB-C adapter | Raspberry Pi Foundation | $15 |

**Core Subtotal: $200**

### **Cable Box Electronics**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| TM1637 LED Display Board | 4-digit channel number display | Amazon/AliExpress | $5 |
| 3x4 Matrix Keypad | Channel number entry | Amazon/AliExpress | $8 |
| Jumper Wires (Male-Female) | GPIO connections | Amazon | $5 |
| M2.5 Screws & Nuts | Pi mounting hardware | Amazon | $5 |
| Hook-up Wire | Internal connections | Amazon | $5 |

**Electronics Subtotal: $28**

### **Video Output & CRT Connection**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| HDMI to Composite Adapter | Convert Pi HDMI to CRT input | Amazon | $15 |
| Composite Video Cable | RCA connections to CRT | Amazon | $5 |
| HDMI Cable (Short) | Pi to adapter connection | Amazon | $5 |

**Video Subtotal: $25**

### **3D Printing Materials**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| PLA Filament | ~200g for cable box | Amazon/Local | $10 |
| Support Material | If using dissolvable supports | Amazon | $5 |

**3D Printing Subtotal: $15**

### **Optional Components**
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| Heat Sinks | Pi 5 cooling (recommended) | Amazon | $8 |
| Case Fan (30mm) | Active cooling if needed | Amazon | $10 |
| IR Receiver Module | For TV remote compatibility | Amazon | $5 |
| Bluetooth Dongle | If Pi 5 built-in insufficient | Amazon | $8 |

**Optional Subtotal: $31**

## **Total Project Cost: $299** (with all options)
## **Minimum Build Cost: $268** (core + required components)

## Hardware Assembly Components

### **From Shane Mason's Cable Box Repo**

#### **3D Printed Parts**
- **CableBox-main.stl** - Main box, trim pieces, foot screws
- **CableBox-bottom.stl** - Bottom panel of the box
- **Print Settings**: PLA with 0.4mm nozzle recommended
- **Infill**: 15-20% for good strength vs material usage

#### **Electronic Connections**

**TM1637 LED Display to Pi 5:**
| TM1637 Pin | Pi 5 GPIO Pin | Wire Color |
|------------|---------------|------------|
| VCC | 3.3V (Pin 1) | Red |
| GND | Ground (Pin 6) | Black |
| DIO | GPIO 2 (Pin 3) | Blue |
| CLK | GPIO 3 (Pin 5) | Yellow |

**3x4 Matrix Keypad to Pi 5:**
| Keypad Pin | Pi 5 GPIO Pin | Function |
|------------|---------------|----------|
| Pin 1 | GPIO 26 | Row 0 |
| Pin 2 | GPIO 19 | Row 1 |
| Pin 3 | GPIO 13 | Row 2 |
| Pin 4 | GPIO 6 | Row 3 |
| Pin 5 | GPIO 5 | Col 0 |
| Pin 6 | GPIO 11 | Col 1 |
| Pin 7 | GPIO 9 | Col 2 |

### **Pi 5 Mounting**
- **Mounting Posts**: Built into 3D printed case
- **Hardware**: M2.5 nuts embedded in posts with superglue
- **Screws**: M2.5 x 6mm to secure Pi to posts
- **Cooling**: Essential to use active cooling with enclosed case

## CRT Television Connection

### **Video Signal Conversion**
Most CRT TVs from the 90s accept composite video (yellow RCA jack) or RF (coaxial/antenna) input. The Pi 5's HDMI output needs conversion:

📺 **For complete CRT setup instructions, see [CRT Integration Guide](CRT_INTEGRATION.md)**

#### **HDMI to Component (Recommended for late 90s+ CRTs)**
- **Adapter**: HDMI to Component converter ($15-35)
- **Quality**: Excellent video quality, progressive scan
- **Compatibility**: Works with CRTs that have Red/Blue/Green inputs
- **Best for**: Ultimate image quality and authenticity

#### **HDMI to Composite (Budget option for all CRTs)**
- **Adapter**: HDMI to RCA converter (~$12)
- **Quality**: Good video quality, simple connection
- **Latency**: Minimal delay for authentic feel
- **Compatibility**: Works with ALL CRT TVs (yellow/red/white inputs)

### **Video Configuration Options**

#### **Component Video (480p/720p)**
```bash
# Pi 5 config.txt for component output
hdmi_group=1
hdmi_mode=4        # 720x480 60Hz (480p)
hdmi_cvt=720 480 60 1 0 0 0
config_hdmi_boost=4
```

#### **Composite Video (480i)**
```bash
# Pi 5 config.txt for composite output  
hdmi_group=2
hdmi_mode=87
hdmi_cvt=640 480 60 1 0 0 0  # 4:3 aspect ratio
hdmi_drive=1
config_hdmi_boost=4
```

## Assembly Process

### **Step 1: 3D Printing**
1. Download STL files from Shane Mason's cable-box repository
2. Print CableBox-main.stl and CableBox-bottom.stl
3. Use 15-20% infill with PLA filament
4. Print time: ~8-12 hours total

### **Step 2: Electronics Preparation**
1. Embed M2.5 nuts in mounting posts with superglue
2. Let cure completely before proceeding
3. Prepare jumper wires with proper connections
4. Test TM1637 display and keypad before assembly

### **Step 3: Pi Installation**
1. Install heat sink on Pi 5 CPU
2. Mount Pi 5 to case using M2.5 screws
3. Connect HDMI pigtail and route through case opening
4. Connect power cable and route through case

### **Step 4: Component Wiring**
1. Connect TM1637 display according to pin diagram
2. Connect 3x4 matrix keypad to GPIO pins
3. Use strain relief for external cables
4. Test all connections before final assembly

### **Step 5: Software Setup**
1. Install FieldStation42 on Pi 5
2. Configure keypad input handling
3. Set up LED display control
4. Test channel switching functionality

## Advantages Over Custom Hardware

### **Cost Benefits**
- **$268 vs $589**: 55% cost reduction
- **Proven design**: No prototyping or design iteration needed
- **Standard components**: Easy to source, no custom PCBs
- **Fast assembly**: Weekend build vs weeks of work

### **Technical Benefits**
- **Mature software**: FieldStation42 is proven and documented
- **Active community**: Support and shared configurations
- **Real CRT experience**: Better than LCD emulation
- **Extensible**: Easy to add new features and channels

### **Build Benefits**
- **Simple assembly**: No complex electronics or soldering
- **Standard tools**: Basic 3D printer and hand tools
- **Clear instructions**: Comprehensive documentation available
- **Low risk**: Proven design with known working results

## Required Tools

### **3D Printing**
- **3D Printer**: 200x200mm minimum build volume
- **Filament**: PLA recommended for ease of printing
- **Print bed**: Heated bed helpful but not required

### **Assembly**
- **Screwdriver set**: Phillips head for M2.5 screws
- **Wire strippers**: For jumper wire preparation
- **Multimeter**: For testing connections (optional)
- **Superglue**: For embedding nuts in mounting posts

### **Software Development**
- **SD card reader**: For Pi 5 OS installation
- **HDMI monitor**: For initial Pi setup
- **Keyboard/mouse**: For configuration
- **Network connection**: For software downloads

---
*Hardware platform provides authentic cable box experience with proven reliability and community support*