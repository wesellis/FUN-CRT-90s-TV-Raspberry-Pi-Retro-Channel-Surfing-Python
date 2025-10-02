# Channel Content Guidelines & Standards

## Video File Specifications

### Technical Requirements
- **Container**: MP4 (H.264/AAC)
- **Video Codec**: H.264 (x264)
- **Audio Codec**: AAC stereo
- **Resolution**: 720p maximum (1280×720)
- **Frame Rate**: 29.97 fps (NTSC standard)
- **Aspect Ratio**: 4:3 (cropped/pillarboxed to 960×720)
- **Bitrate**: 1.5-2.5 Mbps video, 128 kbps audio
- **File Size Target**: 100-150MB per 22-minute episode

### Encoding Settings (FFmpeg)
```bash
# Convert any video to 90s TV format
ffmpeg -i input.mkv \
  -c:v libx264 -crf 23 -preset medium \
  -c:a aac -b:a 128k -ar 48000 \
  -vf "scale=960:720:force_original_aspect_ratio=decrease,pad=960:720:(ow-iw)/2:(oh-ih)/2,fps=29.97" \
  -movflags +faststart \
  output.mp4
```

## File Naming Conventions

### TV Shows
```
Format: {show_name}_s{season:02d}e{episode:02d}_{title}.mp4

Examples:
- seinfeld_s03e15_the_suicide.mp4
- friends_s02e08_the_one_with_the_list.mp4
- animaniacs_s01e05_piano_rag.mp4
- rugrats_s01e03_at_the_movies.mp4
```

### Commercials
```
Format: {brand}_{product}_{year}_{variant}.mp4

Examples:
- mcdonalds_happy_meal_1995_batman.mp4
- nintendo_super_mario_64_1996_official.mp4
- surge_soda_1997_fully_loaded.mp4
- taco_bell_fourth_meal_1994_chihuahua.mp4
```

### Station IDs & Bumpers
```
Format: {network}_{type}_{year}_{variant}.mp4

Examples:
- nickelodeon_station_id_1994_splat.mp4
- cartoon_network_bumper_1995_powerhouse.mp4
- mtv_logo_1993_liquid.mp4
- comedy_central_bumper_1996_south_park.mp4
```

## Content Organization Structure

### Directory Layout
```
media/
├── channel_02_sitcoms/
│   ├── shows/
│   │   ├── seinfeld/
│   │   ├── friends/
│   │   ├── cheers/
│   │   └── frasier/
│   └── commercials/
│       ├── 1990-1992/
│       ├── 1993-1995/
│       └── 1996-1999/
│
├── channel_03_cartoons/
│   ├── shows/
│   │   ├── animaniacs/
│   │   ├── ducktales/
│   │   └── gargoyles/
│   └── commercials/
│       └── saturday_morning/
│
└── shared_commercials/
    ├── 90s_ads/
    │   ├── food_beverage/
    │   ├── toys_games/
    │   ├── movies_tv/
    │   └── technology/
    ├── station_ids/
    └── bumpers/
```

## Channel-Specific Content Guidelines

### Channel 2: Sitcoms
**Programming Style**: Classic 90s multi-camera sitcoms with laugh tracks
**Episode Length**: 22-24 minutes
**Commercial Breaks**: 3 breaks (6min, 13min, 20min marks)

**Recommended Shows**:
- **Seinfeld** (1989-1998) - Peak 90s episodes S3-S7
- **Friends** (1994-2004) - Early seasons S1-S4
- **Cheers** (1982-1993) - Later seasons with Rebecca
- **Frasier** (1993-2003) - Peak years S1-S5
- **Home Improvement** (1991-1998) - Tool Time segments
- **Family Matters** (1989-1998) - Urkel years

**Commercial Style**: Mainstream products, family-friendly, upbeat

### Channel 3: Cartoons
**Programming Style**: Saturday morning cartoon block aesthetic
**Episode Length**: 11-22 minutes (varies by show)
**Commercial Breaks**: 2 breaks for 11min, 3 breaks for 22min

**Recommended Shows**:
- **Animaniacs** (1993-1998) - Yakko, Wakko, Dot segments
- **DuckTales** (1987-1990) - Adventure episodes
- **Gargoyles** (1994-1997) - Darker storytelling
- **Batman: The Animated Series** (1992-1995) - Iconic episodes
- **Tiny Toon Adventures** (1990-1992) - Best segments
- **Pinky and the Brain** (1995-1998) - World domination plots

**Commercial Style**: Toys, breakfast cereals, upcoming cartoon movies

### Channel 4: Nicktoons
**Programming Style**: Early Nickelodeon original animation
**Episode Length**: 11-22 minutes
**Commercial Breaks**: Nickelodeon-style shorter breaks

**Recommended Shows**:
- **Rugrats** (1991-2004) - Classic baby adventures S1-S3
- **Doug** (1991-1994) - Original Nickelodeon run only
- **Hey Arnold!** (1996-2004) - Urban adventures
- **Ren & Stimpy** (1991-1996) - Gross-out humor classics
- **Rocko's Modern Life** (1993-1996) - Adult humor disguised
- **Aaahh!!! Real Monsters** (1994-1997) - Monster academy

**Commercial Style**: Nick-specific ads, slime-related products, kid snacks

### Channel 5: Anime
**Programming Style**: Toonami afternoon block (edited for US TV)
**Episode Length**: 22-24 minutes
**Commercial Breaks**: Action figure and video game heavy

**Recommended Shows**:
- **Dragon Ball Z** (1989-1996) - Frieza through Cell sagas
- **Sailor Moon** (1992-1997) - Classic magical girl
- **Ronin Warriors** (1988-1989) - Armored samurai action
- **Voltron** (Reruns) - Classic mecha
- **Speed Racer** (Reruns) - Racing action
- **Thundercats** (Reruns) - Sword and sorcery

**Commercial Style**: Action figures, video games, comic books

### Channel 6: Comedy Central
**Programming Style**: Edgier animated content and stand-up
**Episode Length**: 22-30 minutes
**Commercial Breaks**: Adult-oriented products

**Recommended Shows**:
- **Beavis and Butt-Head** (1993-1997) - Music video commentary
- **South Park** (1997+) - Early seasons only
- **The Critic** (1994-1995) - Movie parodies
- **Dr. Katz** (1995-2002) - Squigglevision animation
- **Stand-up Specials** - 90s comedy stars

**Commercial Style**: Beer, movies, late-night products

### Channel 7: MTV
**Programming Style**: Music videos with occasional reality shows
**Episode Length**: 3-5 minute music videos, 30min reality shows
**Commercial Breaks**: Youth-oriented products

**Recommended Content**:
- **Music Videos** - Alternative rock, grunge, hip-hop, pop
- **MTV News** segments - Kurt Loder reports
- **The Real World** (1992+) - Early seasons
- **Beavis and Butt-Head** - Music video segments
- **120 Minutes** - Alternative music block
- **Yo! MTV Raps** - Hip-hop videos

**Commercial Style**: Soda, jeans, music albums, movie trailers

## Commercial Break Guidelines

### Timing Standards
- **30-minute shows**: 3 breaks at 6min, 13min, 20min
- **60-minute shows**: 5 breaks at 12min, 24min, 36min, 48min, 56min
- **Music videos**: 1 break per 3-4 videos

### Commercial Selection Rules
1. **Era appropriate**: 1990-1999 only
2. **Channel appropriate**: Match demographic and content style
3. **Variety**: Rotate through different product categories
4. **Authentic**: Original broadcast commercials preferred
5. **Quality**: Clear audio, good video quality

### Break Composition
```
Standard 3-commercial break:
1. Product commercial (30 seconds)
2. Movie/TV trailer (30 seconds)  
3. Product commercial (30 seconds)
Total: ~90 seconds
```

## Content Acquisition Sources

### Legal Sources
- **Personal DVD collections** - Rip owned content
- **Streaming services** - Screen capture (personal use)
- **YouTube** - Official uploads and fair use content
- **Internet Archive** - Public domain and fair use materials
- **Library collections** - DVD borrowing and ripping

### Commercial Archives
- **YouTube channels**: Commercial Vault, RetroCommercials
- **Internet Archive**: Television commercial collections
- **Personal recordings**: VHS transfers from era
- **Fan sites**: Dedicated 90s commercial preservation

## Quality Control Checklist

### Video Quality
- [ ] Resolution exactly 960×720 (4:3 in 720p frame)
- [ ] Frame rate 29.97 fps
- [ ] No interlacing artifacts
- [ ] Clean, stable image
- [ ] Proper color saturation (not oversaturated)

### Audio Quality
- [ ] Stereo AAC at 128 kbps
- [ ] Normalized volume levels across all content
- [ ] No audio clipping or distortion
- [ ] Consistent volume between shows and commercials
- [ ] Clear dialogue and sound effects

### File Management
- [ ] Correct naming convention followed
- [ ] Organized in proper directory structure
- [ ] File size within 100-150MB target
- [ ] Fast start enabled for streaming
- [ ] Metadata properly tagged

### Content Validation
- [ ] Era appropriate (1990-1999)
- [ ] Channel appropriate content and style
- [ ] Complete episodes (no cut-off content)
- [ ] Commercials match programming demographic
- [ ] No modern elements visible (logos, graphics, etc.)

---
*Content guidelines ensure authentic 90s TV experience with professional quality standards*