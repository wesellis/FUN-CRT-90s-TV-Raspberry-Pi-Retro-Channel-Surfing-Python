#!/usr/bin/env python3
"""
90s CRT TV - Main Application Entry Point
Authentic retro TV experience with channel surfing
"""

import sys
import os
from core.tv_controller import TVController

def main():
    """Main application entry point"""
    print("🖥️  90s CRT TV Starting...")
    print("📺 Channels: Sitcoms, Cartoons, Anime, Weather, Games & More!")
    
    try:
        # Initialize TV controller
        tv = TVController()
        
        # Start the TV experience
        tv.power_on()
        tv.run()
        
    except KeyboardInterrupt:
        print("\n📺 TV Powered Off - Thanks for watching!")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
