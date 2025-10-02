# Pi Terminal Project - Complete Bill of Materials

**Source Project**: [Pi Terminal by sb-ocr](https://github.com/sb-ocr/pi-terminal)
- **Thingiverse**: https://www.thingiverse.com/thing:5865117  
- **Instructables**: https://www.instructables.com/Making-a-Retro-Inspired-Raspberry-Pi-Enclosure-por/

## Electronics Components

### Main Computing & Display
| Component | Description | Source | Est. Price |
|-----------|-------------|---------|------------|
| Raspberry Pi 4 | Base model (upgrade to Pi 5 for our project) | [Rpilocator](https://rpilocator.com/) | $80 |
| Raspberry Pi Low-Profile CPU Cooler | Essential for enclosed build | [Amazon](https://geni.us/jZGuZt9) | $15 |
| 8" IPS LCD HJ080IA-01E | With driver board, perfect for retro TV | [Aliexpress](https://s.click.aliexpress.com/e/_DmC2qmH) / [Amazon](https://geni.us/ZfU1Y) | $70 |
| Custom PCBs (set of 3) | Control panel, power adapter, main board | [PCBWay](https://pcbway.com/g/TC4KGU) | $50 |

### Power & UPS System
| Component | Description | Source | Est. Price |
|-----------|-------------|---------|------------|
| Pi-UpTime UPS 2.0 | Battery backup for portable operation | [Amazon](https://geni.us/zOOjE) | $60 |
| 2 × 18650 Li-Ion | 3400mAh unprotected batteries | Electronics suppliers | $20 |

### Connectivity
| Component | Description | Source | Est. Price |
|-----------|-------------|---------|------------|
| HDMI Switcher 2 in 1 Out | For dual input capability | [Amazon](https://geni.us/OfXlV) | $15 |
| Hook-up Wire | Various colors for internal wiring | [Amazon](https://geni.us/8hiS) | $10 |
| Dupont Connectors | For modular connections | [Amazon](https://geni.us/AMdor) | $8 |

### HDMI Cables & Adapters
| Component | Description | Source | Est. Price |
|-----------|-------------|---------|------------|
| 1 × Micro HDMI to Standard Plug | Pi to switcher | [Adafruit](https://www.adafruit.com/product/3557) | $8 |
| 1 × Micro HDMI to Standard Socket | Extension/routing | [Aliexpress](https://s.click.aliexpress.com/e/_DeT0a9b) | $5 |
| 1 × Standard HDMI Plug to Socket | Panel mount connection | Various | $6 |
| 1 × Standard HDMI Plug to Plug | Internal routing | Various | $5 |
| Micro to Micro USB cable (short) | Power routing | Various | $3 |
| 3.5mm Audio cable (short) | Audio connections | Various | $3 |

**Electronics Subtotal: ~$358**

## Control Panel Components
**Complete BOM**: [Digikey T2WYT5REPG](https://www.digikey.ca/en/mylists/list/T2WYT5REPG)

### Switches & Controls
| Component | Quantity | Description | Digikey Part |
|-----------|----------|-------------|--------------|
| Pushbutton Switch DPST-NO | 6 | Main channel controls | TBD |
| Pushbutton Switch DPDT | 1 | Power/mode toggle | TBD |
| Round Switch Cap | 7 | Button caps for professional look | TBD |
| Rocker Switch SPST | 1 | Panel mount power switch | TBD |

### Electronic Components
| Component | Quantity | Description | Package |
|-----------|----------|-------------|---------|
| Resistors 100 Ohms | 2 | Current limiting | 0603 (1608 Metric) |
| Resistors 5.1 kOhms | 2 | Pull-up resistors | 0603 (1608 Metric) |
| Green LEDs | 3 | Status indicators | 1206 (3016 Metric) Vf 2.1V |

### Audio & Connectivity
| Component | Quantity | Description |
|-----------|----------|-------------|
| 4 Ohm 2W Small Speakers | 2 | Built-in audio |
| 3.5mm Switched Headphone Jack | 2 | Audio output options |
| Header Connector 20 position | 1 | 2×10 - 2.54mm |
| Header Connector 4 position | 1 | 2×2 - 2.54mm |

**Control Panel Subtotal: ~$45**

## Power Adapter Board
**Complete BOM**: [Digikey 3XV4R3BO7A](https://www.digikey.ca/en/mylists/list/3XV4R3BO7A)

| Component | Quantity | Description |
|-----------|----------|-------------|
| USB-C Receptacle Connector | 2 | 24 pin charging only |
| USB Micro-B Receptacle | 1 | Standard charging port |
| 2 Position Terminal Block | 1 | Power connections |
| Header Connector 2 position | 1 | 1×2 - 2.54mm |
| Jumper Connector | 1 | 1×2 - 2.54mm |

**Power Adapter Subtotal: ~$25**

## Hardware & Fasteners

### Heat-Set Inserts
| Component | Quantity | Size | McMaster Part | Est. Price |
|-----------|----------|------|---------------|------------|
| Heat-Set Inserts | 21 | M2.5 × 3.4mm | [94180A321](https://www.mcmaster.com/94180A321/) | $15 |
| Heat-Set Inserts | 8 | M4 × 8mm | [94180A353](https://www.mcmaster.com/94180A353/) | $10 |
| Tripod Insert | 1 | 1/4"-20, 0.3" Length | [93365A160](https://www.mcmaster.com/93365A160/) | $3 |

### Handles & Thumb Screws
| Component | Quantity | Description | McMaster Part | Est. Price |
|-----------|----------|-------------|---------------|------------|
| Mini Pull Handles | 2 | 3/4" Center-to-Center | [1726A112](https://www.mcmaster.com/1726A112/) | $8 |
| Thumb Screws | 4 | M4 x 6-10mm | [99607A276](https://www.mcmaster.com/99607A276/) | $10 |

### Machine Screws
| Component | Quantity | Size | Source | Est. Price |
|-----------|----------|------|--------|------------|
| Socket Head Screws | 13 | M2.5 x 5mm | [Amazon](https://geni.us/t4BmSQ) | $8 |
| Socket Head Screws | 3 | M2.5 x 8mm | [Amazon](https://geni.us/t4BmSQ) | $3 |
| Socket Head Screws | 5 | M2.5 x 20mm | [Amazon](https://geni.us/t4BmSQ) | $5 |
| Flat Head Screws | 3 | M2.5 x 5-6mm | Various | $2 |
| M2.5 Nylon Spacer Standoffs | Various | Spacing and isolation | [Amazon](https://geni.us/jIyiM) | $10 |

**Hardware Subtotal: ~$74**

## 3D Printing & Finishing Materials

### Printing Materials
| Component | Quantity | Description | Source | Est. Price |
|-----------|----------|-------------|--------|------------|
| PLA Filament | 1 spool | ~1kg for complete build | [Amazon](https://geni.us/XkGsy) | $25 |

### Finishing Supplies
| Component | Description | Source | Est. Price |
|-----------|-------------|--------|------------|
| Assorted Grits Sandpaper | 220, 320, 400, 600 grit | [Amazon](https://geni.us/turnM3) | $15 |
| Glazing and Spot Putty | Fill print lines and imperfections | [Amazon](https://geni.us/3jiw9) | $8 |
| Filler Primer (sandable) | Base coat for paint | [Amazon](https://geni.us/1BAKZ) | $12 |
| Spray Paint | Color matched to retro TV aesthetic | [Amazon](https://geni.us/I7qjJ) | $15 |
| Flat Matte Clear Coat | Professional finish protection | [Amazon](https://geni.us/Cywvbo) | $12 |

**3D Printing & Finishing Subtotal: ~$87**

## Required Tools

### Electronics Tools
| Tool | Description | Source | Est. Price |
|------|-------------|--------|------------|
| Soldering Station/Iron | Temperature controlled | [Amazon](https://geni.us/16zcw5) | $40 |
| Helping Hands | Third hand for soldering | [Amazon](https://geni.us/qmbA3W) | $15 |
| Precision Screwdriver Set | Various sizes for electronics | [Amazon](https://geni.us/pE8dvKd) | $20 |
| Wire Stripper | For hookup wire prep | [Amazon](https://geni.us/ujTOmu) | $12 |
| Crimping Tools | Dupont connector assembly | [Amazon](https://geni.us/79yu8a) | $25 |

### Assembly Tools & Supplies
| Tool | Description | Source | Est. Price |
|------|-------------|--------|------------|
| 3D Printer | Min 200×200mm build surface | [Amazon](https://geni.us/UKTApo) | $200+ |
| Sanding Block | For smooth finishing | Hardware store | $5 |
| Flux, Solder, Heat Shrink | Electronics assembly | Various | $15 |
| Flush Cutters | Wire and component trimming | Various | $10 |
| Hobby Knife | Precision cutting | Various | $5 |
| Tweezers and Pliers | Fine assembly work | Various | $15 |
| Isopropyl Alcohol | Cleaning flux residue | Various | $3 |

**Tools Subtotal: ~$365** (if purchasing new)

## Total Project Cost Summary

| Category | Subtotal |
|----------|----------|
| Electronics | $358 |
| Control Panel | $45 |
| Power Adapter | $25 |
| Hardware & Fasteners | $74 |
| 3D Printing & Finishing | $87 |
| **TOTAL MATERIALS** | **$589** |
| Tools (if needed) | $365 |
| **GRAND TOTAL** | **$954** |

## Cost Optimization Options

### Budget Reductions
- **Skip UPS system**: -$80 (lose portable operation)
- **Single USB-C port**: -$10 (reduce charging flexibility)
- **Basic finish**: -$30 (primer and single color only)
- **Fewer control buttons**: -$20 (simplify control panel)

### **Optimized Build Cost: ~$450-500**

## Notes & Considerations

### Optional Components
⚠️ **Some parts are optional depending on configuration:**
- UPS system only needed for portable operation
- Dual USB-C ports provide charging flexibility
- All hardware quantities assume full-featured build

### Sourcing Strategy
- **Electronics**: Order early due to potential shipping delays
- **Hardware**: McMaster-Carr for reliable sourcing
- **3D Printing**: Can substitute materials based on availability
- **Tools**: Many makers already own basic tools

### Build Time Estimates
- **3D Printing**: 40-60 hours print time
- **Electronics Assembly**: 8-12 hours
- **Finishing**: 6-10 hours (including cure times)
- **Software Setup**: 4-8 hours
- **Total Project Time**: 60-90 hours

---
*Complete BOM provides professional foundation for 90s TV project hardware*