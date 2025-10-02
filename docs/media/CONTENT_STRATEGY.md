# Media Content Strategy & Organization

## Content Overview
The 90s CRT TV experience requires carefully curated content that captures the authentic feel of 1990s television programming, including shows, commercials, and transitional elements.

## Video Specifications

### Technical Requirements
- **Format**: MP4 with H.264 encoding
- **Resolution**: 720p maximum (optimized for 8" display)
- **Aspect Ratio**: 4:3 preferred (authentic 90s TV)
- **File Size**: 100-150MB per episode
- **Bitrate**: 1-2 Mbps (balance quality vs. storage)
- **Audio**: AAC stereo, normalized levels (-23 LUFS)
- **Frame Rate**: 29.97 fps (NTSC standard)

### Video Processing Pipeline
```bash
# Convert to optimal format using FFmpeg
ffmpeg -i input.avi \
  -c:v libx264 -preset medium -crf 23 \
  -c:a aac -b:a 128k \
  -vf "scale=960:720,setsar=1:1" \
  -r 29.97 \
  output.mp4
```

## Channel Content Strategy

### Channel 2: Sitcoms
**Target Shows:**
- **Seinfeld** (1989-1998) - Peak 90s comedy
- **Friends** (1994-2004) - Essential 90s culture
- **Cheers** (1982-1993) - Late-run episodes
- **Frasier** (1993-2004) - Sophisticated humor
- **Home Improvement** (1991-1998) - Family sitcom
- **Full House** (1987-1995) - Family-friendly content

**Episode Selection Strategy:**
- Focus on syndication-popular episodes
- Avoid very special episodes or multi-parters
- Mix different seasons for variety
- Include holiday episodes seasonally

### Channel 3: Saturday Morning Cartoons
**Target Shows:**
- **Animaniacs** (1993-1995) - Warner Bros. flagship
- **DuckTales** (1987-1990) - Disney afternoon
- **Gargoyles** (1994-1997) - Serious animated drama
- **Batman: The Animated Series** (1992-1995)
- **X-Men** (1992-1997) - Marvel's animated success
- **Spider-Man** (1994-1998)

**Programming Notes:**
- Saturday morning block feel (6AM-12PM schedule)
- Mix educational content with entertainment
- Include classic Disney shorts as filler

### Channel 4: Nicktoons
**Target Shows:**
- **Rugrats** (1991-2004) - Original Nicktoon
- **Doug** (1991-1994) - Relatable childhood stories
- **Hey Arnold!** (1996-2004) - Urban kid stories
- **Ren & Stimpy** (1991-1996) - Edgy animation
- **Rocko's Modern Life** (1993-1996)
- **AAAHH!!! Real Monsters** (1994-1997)

**Brand Integration:**
- Include Nickelodeon bumpers and IDs
- "Nick at Nite" programming for evening hours
- Classic Nick game shows as filler

### Channel 5: Anime/Toonami
**Target Shows:**
- **Dragon Ball Z** (1989-1996) - Toonami flagship
- **Sailor Moon** (1992-1997) - Magical girl essential
- **Ronin Warriors** (1988-1989) - Mecha action
- **Mobile Suit Gundam Wing** (1995-1996)
- **Tenchi Muyo!** (1992-1995)
- **Outlaw Star** (1998) - Space western

**Programming Strategy:**
- Weekday afternoon Toonami block (4PM-6PM)
- Saturday night anime movies
- Include Toonami bumpers and music videos
- Tom (robot host) segments if available

### Channel 6: Comedy Central
**Target Shows:**
- **Beavis and Butt-Head** (1993-1997) - Network defining
- **South Park** (1997-present) - Early seasons only
- **Mystery Science Theater 3000** (1988-1999)
- **The State** (1993-1995) - Sketch comedy
- **Strangers with Candy** (1999-2000)

**Content Notes:**
- Stand-up comedy specials
- Classic movies with commentary
- "Comedy Central Presents" stand-up shows

### Channel 7: MTV
**Target Content:**
- **Music Videos** - 90s hits across genres
- **The Real World** (1992-present) - Early seasons
- **Beavis and Butt-Head** (music video commentary)
- **MTV Unplugged** sessions
- **120 Minutes** alternative music
- **Headbangers Ball** metal programming

**Music Video Categories:**
- Grunge: Nirvana, Pearl Jam, Soundgarden
- Pop: Britney Spears, Backstreet Boys, *NSYNC
- Hip-Hop: Tupac, Biggie, Wu-Tang Clan
- Alternative: Radiohead, Beck, Weezer
- Electronic: Prodigy, Chemical Brothers

### Channel 8: Weather Channel
**Content Source:** Weather Star 4000+ recreation
- Real-time weather data
- Local forecasts with smooth jazz
- Radar imagery and animations
- Travel conditions
- "Local on the 8s" programming
- Seasonal weather programming

### Channel 9: Gaming
**Platform:** EmulationStation/RetroArch
- NES library (Super Mario, Zelda, Metroid)
- SNES games (Super Mario World, Chrono Trigger)
- Genesis titles (Sonic, Streets of Rage)
- Game Boy/Game Boy Color
- Early PlayStation games

## Commercial Content Strategy

### 90s Commercial Categories

**Fast Food & Restaurants:**
- McDonald's (Happy Meal toys, McNuggets)
- Taco Bell ("Yo Quiero" Chihuahua campaigns)
- Pizza Hut (Personal Pan Pizza, Stuffed Crust)
- Burger King (Have It Your Way campaigns)
- KFC (Colonel Sanders focus)

**Snack Foods & Beverages:**
- Surge soda (Coca-Cola's Mountain Dew competitor)
- Bagel Bites ("Pizza in the morning...")
- Hot Pockets (microwave convenience)
- Dunkaroos cookies
- Crystal Pepsi (short-lived clear cola)
- Fruitopia (psychedelic Coca-Cola brand)

**Toys & Games:**
- Nintendo 64 launch campaigns
- Tamagotchi virtual pets
- Tickle Me Elmo phenomenon
- Super Soaker water guns
- Pogs/Milk Caps craze
- Beanie Babies collecting

**Technology:**
- AOL Internet service ("You've Got Mail")
- Computers (Gateway cow boxes, iMac)
- Cell phones (early mobile adoption)
- CD players and Walkmans
- Early gaming systems

**Movie Trailers:**
- Jurassic Park (1993)
- The Lion King (1994)
- Toy Story (1995)
- Independence Day (1996)
- Titanic (1997)
- The Matrix (1999)

### Commercial Timing Strategy
```python
# Commercial break timing (authentic to 90s TV)
SITCOM_BREAKS = [
    (6*60, 120),    # 6 minutes in, 2 minute break
    (14*60, 150),   # 14 minutes in, 2.5 minute break
    (22*60, 120)    # End of episode, 2 minutes
]

HOUR_SHOW_BREAKS = [
    (12*60, 180),   # 12 minutes in, 3 minute break
    (25*60, 240),   # 25 minutes in, 4 minute break  
    (38*60, 180),   # 38 minutes in, 3 minute break
    (50*60, 180)    # End break, 3 minutes
]
```

## Station IDs & Bumpers

### Network Branding Elements
- **Network logos** and animated IDs
- **"We'll be right back"** transition graphics
- **"And now back to..."** return graphics
- **Time/temperature** lower thirds
- **Programming announcements** ("Coming up next...")
- **Technical difficulties** placeholder content

### Seasonal Content
- **Holiday specials** during appropriate times
- **Summer movie** promotions
- **Back-to-school** themed programming
- **Halloween/Christmas** special episodes

## Content Acquisition Strategy

### Legal Considerations
- Use content you own on physical media
- Focus on public domain or freely available content
- Create original commercials and bumpers
- Use copyright-free music for transitions

### File Organization
```
media/
├── channel_02_sitcoms/
│   ├── shows/
│   │   ├── seinfeld/
│   │   │   ├── seinfeld_s03e01.mp4
│   │   │   └── seinfeld_s03e02.mp4
│   │   └── friends/
│   └── commercials/
├── shared_commercials/
│   ├── 90s_ads/
│   │   ├── fast_food/
│   │   ├── toys/
│   │   └── movies/
│   ├── station_ids/
│   └── bumpers/
└── audio/
    ├── commercial_music/
    └── transition_sounds/
```

### Naming Conventions
- **Shows**: `showname_s##e##.mp4` (seinfeld_s03e15.mp4)
- **Commercials**: `brand_product_year.mp4` (mcdonalds_happymeal_1995.mp4)
- **Station IDs**: `network_type_variant.mp4` (nick_logo_slime.mp4)
- **Bumpers**: `network_transition_type.mp4` (mtv_be_right_back.mp4)

## Quality Control Standards

### Video Quality Checks
- Consistent audio levels across all content
- Color correction for authentic TV look
- Aspect ratio consistency (4:3 preferred)
- No digital artifacts or compression issues
- Smooth transitions between segments

### Content Curation
- Age-appropriate content mixing
- Historical accuracy to 90s programming
- Balanced genre representation
- Authentic commercial-to-content ratios
- Seasonal relevance and timing

---
*Content strategy designed to recreate authentic 90s television experience*
