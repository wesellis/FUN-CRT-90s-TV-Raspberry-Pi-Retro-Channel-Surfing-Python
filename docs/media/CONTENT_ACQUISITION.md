# Content Acquisition & Management Strategy

## Legal Considerations & Best Practices

### Personal Use Guidelines
This project is designed for **personal, non-commercial use only**. All content acquisition should follow these principles:

1. **Own before you rip**: Only digitize content you legally own on DVD/VHS
2. **Personal viewing**: Content is for your own use and close friends/family
3. **No distribution**: Do not share or sell content files
4. **Fair use**: Small portions for demonstration purposes may qualify as fair use
5. **Respect copyright**: Always credit original creators and networks

### Recommended Legal Sources
- **Personal DVD/Blu-ray collection**: Rip your owned media
- **Streaming services**: Screen capture for personal backup (check ToS)
- **Public domain**: Internet Archive and similar repositories
- **Fair use**: Brief clips for educational/transformative purposes

## Content Sourcing Strategy

### Phase 1: Foundation Content (Week 1-2)
**Goal**: Get 2-3 hours per channel for initial testing

#### Priority Shows (1-2 episodes each)
```
Channel 2 (Sitcoms):
- Seinfeld: "The Contest", "The Marine Biologist"
- Friends: "The One with the Embryos", "The One with Ross's Wedding"

Channel 3 (Cartoons):
- Animaniacs: "Yakko's World", "Good Idea/Bad Idea" segments
- DuckTales: "Treasure of the Golden Suns" pilot

Channel 4 (Nicktoons):
- Rugrats: "Tommy's First Birthday", "The Turkey Who Came to Dinner"
- Doug: "Doug Bags a Neematoad", "Doug's 1st Movie"

Channel 5 (Anime):
- Dragon Ball Z: "The Arrival of Raditz", "Goku vs. Vegeta"
- Sailor Moon: "A Moon Star is Born", "Talk Radio"
```

#### Essential Commercials (10-15 each category)
- **Food & Beverage**: McDonald's, Taco Bell, Surge, Bagel Bites
- **Toys & Games**: Nintendo 64, Furby, Super Soaker, Tamagotchi
- **Movies**: Toy Story, Jurassic Park, The Lion King trailers
- **Technology**: AOL, Gateway computers, Nokia phones

### Phase 2: Content Expansion (Week 3-8)
**Goal**: Build 20+ hours per channel

#### Full Season Priorities
1. **Seinfeld Seasons 4-6** (peak quality years)
2. **Friends Seasons 1-3** (classic early episodes)
3. **Animaniacs Season 1** (best segments)
4. **Rugrats Seasons 1-2** (original babies)
5. **Dragon Ball Z Frieza Saga** (iconic episodes)

#### Commercial Library Expansion
- **100+ commercials per category**
- **Network-specific content** (Nickelodeon vs MTV style)
- **Seasonal content** (Christmas, Halloween, summer)
- **PSAs and educational content** (Just Say No, etc.)

### Phase 3: Polish & Specialization (Week 9+)
**Goal**: Deep content library with rare finds

#### Specialty Content
- **Holiday specials** for appropriate seasons
- **Network bumpers and station IDs**
- **Local commercial content** (if available)
- **Crossover episodes and special events**
- **Behind-the-scenes content** for variety

## Content Acquisition Workflow

### Video Acquisition Process

#### DVD/Blu-ray Ripping
```bash
# Install required tools
sudo apt install makemkv handbrake-cli

# Step 1: Extract with MakeMKV (preserves quality)
makemkv dvd:0 /output/folder --minlength=20

# Step 2: Convert with HandBrake
HandBrakeCLI -i input.mkv -o output.mp4 \
  --preset="Fast 720p30" \
  --crop 0:0:0:0 --loose-anamorphic \
  --modulus 2 --x264-profile high \
  --h264-level 4.0
```

#### Streaming Capture Setup
```bash
# OBS Studio settings for streaming capture
# Video: 1280x720, 30fps
# Audio: 48kHz stereo
# Encoder: x264, CRF 18-23
# Output: MP4 container
```

### Commercial Hunting Strategy

#### YouTube Sources
- **Official brand channels**: Often have commercial archives
- **Retro commercial compilations**: "90s Commercial Breaks"
- **TV recording channels**: Full broadcast recordings
- **Fan preservation projects**: Dedicated archivists

#### Search Terms That Work
```
"90s commercials compilation"
"1995 TV commercial break"
"Saturday morning commercials 1994"
"Nickelodeon commercial break 1993"
"MTV commercial 1997"
"[brand name] commercial 1990s"
```

### Content Processing Pipeline

#### Batch Processing Script
```python
#!/usr/bin/env python3
"""
Content processing pipeline for 90s TV project
Handles video conversion, naming, and organization
"""

import os
import subprocess
import json
from pathlib import Path

def process_video_batch(input_dir, output_dir, content_type):
    """Process multiple videos with consistent settings"""
    
    # Standard encoding settings
    encoding_params = [
        '-c:v', 'libx264', '-crf', '23',
        '-c:a', 'aac', '-b:a', '128k',
        '-vf', 'scale=960:720:force_original_aspect_ratio=decrease,pad=960:720:(ow-iw)/2:(oh-ih)/2',
        '-r', '29.97',
        '-movflags', '+faststart'
    ]
    
    for video_file in Path(input_dir).glob('*.mkv'):
        output_file = Path(output_dir) / f"{video_file.stem}.mp4"
        
        cmd = ['ffmpeg', '-i', str(video_file)] + encoding_params + [str(output_file)]
        subprocess.run(cmd, check=True)
        
        # Validate output
        if validate_output(output_file):
            print(f"✅ Processed: {output_file}")
        else:
            print(f"❌ Failed: {output_file}")

def validate_output(video_file):
    """Check if output meets quality standards"""
    # Check file size (should be 100-150MB for 22min episode)
    # Check resolution (should be 960x720)
    # Check duration (should match source)
    return True  # Simplified for example
```

### Quality Control Standards

#### Video Quality Checklist
- [ ] **Resolution**: Exactly 960×720 (4:3 aspect ratio)
- [ ] **Frame rate**: 29.97 fps (NTSC standard)
- [ ] **Bitrate**: 1.5-2.5 Mbps (good quality, reasonable file size)
- [ ] **Audio sync**: Perfect lip sync throughout
- [ ] **Color**: Natural, not oversaturated
- [ ] **Artifacts**: No compression artifacts or blocky areas

#### Content Quality Standards
- [ ] **Complete episodes**: No missing segments or cut-offs
- [ ] **Era appropriate**: 1990-1999 content only
- [ ] **Broadcast quality**: TV-aired versions preferred
- [ ] **Language**: Original English audio
- [ ] **Censorship**: Broadcast TV standards (not cable/uncut)

### File Organization System

#### Automated Organization
```python
def organize_content(source_dir, media_root):
    """Automatically organize content by type and channel"""
    
    organization_rules = {
        'sitcom': 'channel_02_sitcoms/shows',
        'cartoon': 'channel_03_cartoons/shows', 
        'nicktoon': 'channel_04_nicktoons/shows',
        'anime': 'channel_05_anime/shows',
        'commercial': 'shared_commercials/90s_ads',
        'station_id': 'shared_commercials/station_ids'
    }
    
    for file_path in Path(source_dir).rglob('*.mp4'):
        content_type = detect_content_type(file_path.name)
        target_dir = Path(media_root) / organization_rules[content_type]
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Move and rename file
        new_path = target_dir / standardize_filename(file_path.name)
        file_path.rename(new_path)
```

### Commercial Break Assembly

#### Creating Authentic Breaks
```python
def create_commercial_break(channel_type, duration_target=90):
    """Assemble realistic commercial breaks"""
    
    commercial_pools = {
        'sitcom': ['mcdonalds_happy_meal_1995.mp4', 'surge_soda_1997.mp4'],
        'cartoon': ['nintendo_64_1996.mp4', 'frosted_flakes_1994.mp4'],
        'nicktoon': ['nickelodeon_slime_1995.mp4', 'gak_1992.mp4']
    }
    
    # Select 2-3 commercials that total ~90 seconds
    selected_commercials = select_commercials(
        commercial_pools[channel_type], 
        target_duration=duration_target
    )
    
    # Add fade transitions between commercials
    return add_commercial_transitions(selected_commercials)
```

## Content Database & Metadata

### Episode Tracking System
```json
{
  "episodes": {
    "seinfeld_s04e16_the_shoes": {
      "title": "The Shoes",
      "season": 4,
      "episode": 16,
      "air_date": "1993-02-04",
      "duration": 1320,
      "file_path": "channel_02_sitcoms/shows/seinfeld/seinfeld_s04e16_the_shoes.mp4",
      "commercial_breaks": [360, 720, 1080],
      "quality_checked": true,
      "era_appropriate": true
    }
  },
  "commercials": {
    "mcdonalds_happy_meal_1995_batman": {
      "brand": "McDonald's",
      "product": "Happy Meal",
      "year": 1995,
      "duration": 30,
      "categories": ["food", "toys", "kids"],
      "appropriate_for": ["sitcom", "cartoon", "nicktoon"]
    }
  }
}
```

### Content Statistics Dashboard
```python
def generate_content_report():
    """Create overview of available content"""
    
    stats = {
        'total_episodes': count_episodes(),
        'total_commercials': count_commercials(),
        'content_hours_by_channel': calculate_channel_hours(),
        'quality_control_status': check_quality_status(),
        'missing_content_gaps': identify_gaps()
    }
    
    return generate_html_report(stats)
```

## Storage & Backup Strategy

### Storage Requirements
- **Total content goal**: 200+ hours (100GB+ at 720p)
- **Primary storage**: Fast USB 3.0 SSD (1-2TB)
- **Backup storage**: External HDD or cloud storage
- **Working storage**: Local PC drive for processing

### Backup Strategy
```bash
# Automated backup script
#!/bin/bash
rsync -av --progress /media/tv_content/ /backup/tv_content/
rclone sync /media/tv_content/ remote:90s-tv-backup/
```

### Content Versioning
- **Raw captures**: Keep original high-quality captures
- **Processed files**: Final 720p versions for Pi
- **Metadata backups**: JSON databases and playlists
- **Configuration backups**: Channel schedules and settings

---
*Strategic approach to building authentic 90s TV content library while respecting legal boundaries*