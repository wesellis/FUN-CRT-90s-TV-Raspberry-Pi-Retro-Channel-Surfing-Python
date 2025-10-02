# Hardware: Pi Terminal Project Integration

## Base Hardware Platform
**Source**: [Pi Terminal Project](https://www.thingiverse.com/thing:5865117)
- **GitHub**: https://github.com/sb-ocr/pi-terminal
- **Instructables**: https://www.instructables.com/Making-a-Retro-Inspired-Raspberry-Pi-Enclosure-por/

## Core Electronics

### Main Components
- **Raspberry Pi 4** (we'll upgrade to Pi 5)
- **8" IPS LCD** - HJ080IA-01E with Driver Board
  - [Aliexpress](https://s.click.aliexpress.com/e/_DmC2qmH)
  - [Amazon](https://geni.us/ZfU1Y)
- **Custom PCBs** - Order from [PCBWay](https://pcbway.com/g/TC4KGU)
- **Pi-UpTime UPS 2.0** - Battery backup system
- **2 × 18650 Li-Ion Batteries** (3400mAh, unprotected)
- **Raspberry Pi Low-Profile CPU Cooler**

### Connectivity & Switching
- **HDMI Switcher** - 2 in 1 out (potential for dual input)
- **HDMI Cables** - Mix of micro and standard connectors:
  - 1 × Micro HDMI to Standard Plug
  - 1 × Micro HDMI to Standard Socket  
  - 1 × Standard HDMI Plug to Socket
  - 1 × Standard HDMI Plug to Plug
- **Micro to Micro USB cable** (short)
- **3.5mm Audio cable** (short)

## Control Panel Electronics
**Digikey BOM**: [Control Panel Parts](https://www.digikey.ca/en/mylists/list/T2WYT5REPG)

### Components
- **6 × Pushbutton Switches** - DPST-NO (channel controls)
- **1 × Pushbutton Switch** - DPDT (power/mode)
- **7 × Round Switch Caps**
- **3 × Green LEDs** - 1206 (3016 Metric) Vf 2.1V
- **2 × 100 Ohm Resistors** - 0603 (1608 Metric)
- **2 × 4 Ohm 2W Small Speakers**
- **2 × 3.5mm Switched Headphone Jacks**
- **Header Connectors**:
  - 1 × 20 position (2×10 - 2.54mm)
  - 1 × 4 position (2×2 - 2.54mm)

## Power Adapter Board
**Digikey BOM**: [Power Adapter Parts](https://www.digikey.ca/en/mylists/list/3XV4R3BO7A)

### Components
- **2 × 5.1 kOhm Resistors** - 0603 (1608 Metric)
- **1 × Rocker Switch** - SPST Panel Mount
- **2 × USB-C Receptacle Connectors** - 24 pin, charging only
- **1 × USB Micro-B Receptacle**
- **1 × 2 Position Terminal Block**
- **Header Connectors**:
  - 1 × 2 position (1×2 - 2.54mm)
  - 1 × Jumper Connector (1×2 - 2.54mm)

## Hardware & Fasteners

### Heat-Set Inserts
- **21 × M2.5 × 3.4mm** - [McMasterCarr 94180A321](https://www.mcmaster.com/94180A321/)
- **8 × M4 × 8mm** - [McMasterCarr 94180A353](https://www.mcmaster.com/94180A353/)
- **1 × Tripod 1/4"-20** - 0.3" Installed Length [McMasterCarr 93365A160](https://www.mcmaster.com/93365A160/)

### Hardware
- **2 × Mini Pull Handles** - 3/4" Center-to-Center [McMasterCarr 1726A112](https://www.mcmaster.com/1726A112/)
- **4 × Thumb Screws** - M4 x 6-10mm [McMasterCarr 99607A276](https://www.mcmaster.com/99607A276/)

### Screws & Spacers
- **13 × Socket Head Screws** - M2.5 x 5mm
- **3 × Socket Head Screws** - M2.5 x 8mm  
- **5 × Socket Head Screws** - M2.5 x 20mm
- **3 × Flat Head Screws** - M2.5 x 5-6mm
- **M2.5 Nylon Spacer Standoffs** - [Amazon](https://geni.us/jIyiM)

## 3D Printing & Finishing

### Materials
- **PLA Filament** - 1 spool minimum
- **Sandpaper** - Assorted grits
- **Glazing and Spot Putty**
- **Filler Primer** (sandable)
- **Spray Paint** (retro TV colors)
- **Flat Matte Clear Coat**

### Requirements
- **3D Printer** - Minimum 200mm × 200mm build surface
- Standard finishing tools (sanding block, hobby knife, etc.)

## Tool Requirements

### Electronics
- **Soldering Station/Iron**
- **Helping Hands**
- **Wire Strippers**
- **Crimping Tools**
- **Precision Screwdriver Set**
- **Flush Cutters, Pliers, Tweezers**
- **Flux, Solder, Heat Shrink Tubing**
- **Isopropyl Alcohol**

## Cost Estimation
- **Electronics**: ~$200-250
- **Hardware/Fasteners**: ~$30-50
- **3D Printing/Finishing**: ~$20-30
- **Tools** (if needed): ~$100-150
- **Total Project Cost**: ~$300-400

## Modifications for 90s TV Project
1. **Upgrade to Raspberry Pi 5** - Better performance for multiple video streams
2. **Custom software** - Replace their terminal software with our TV controller
3. **IR Receiver** - Add GPIO IR receiver for remote control
4. **Button Mapping** - Use control panel buttons for channel changing
5. **LED Integration** - Use LEDs for channel indicators

## Optional Components
- UPS system (if portable operation desired)
- Second USB-C port (if charging flexibility needed)
- Extra hardware based on specific build configuration

---
*Hardware platform provides professional foundation for 90s TV software*
