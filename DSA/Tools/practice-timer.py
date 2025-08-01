#!/usr/bin/env python3
"""
Interview Practice Timer

A simple tool to help time your coding practice sessions.
Helps build the muscle memory for interview time pressure.

Usage:
    python practice-timer.py --easy        # 15 minute timer
    python practice-timer.py --medium      # 25 minute timer  
    python practice-timer.py --hard        # 35 minute timer
    python practice-timer.py --custom 20   # Custom timer
"""

import time
import sys
import argparse
from datetime import datetime

def display_time(seconds):
    """Convert seconds to MM:SS format"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"

def practice_timer(duration_minutes, problem_type="Custom"):
    """Run a practice timer with motivational messages"""
    total_seconds = duration_minutes * 60
    
    print(f"\n🎯 {problem_type} Problem Timer: {duration_minutes} minutes")
    print("=" * 50)
    print("💡 Tips:")
    print("  1. Read problem twice before coding")
    print("  2. Think about patterns first")
    print("  3. Start with brute force, then optimize")
    print("  4. Test with edge cases")
    print("=" * 50)
    
    input("\n⏱️  Press ENTER to start timer...")
    
    start_time = datetime.now()
    print(f"\n🚀 Timer started at {start_time.strftime('%H:%M:%S')}")
    print("Focus mode: ON! 🔥\n")
    
    try:
        for remaining in range(total_seconds, 0, -1):
            time_str = display_time(remaining)
            
            # Motivational checkpoints
            if remaining == total_seconds // 2:
                print(f"\n⏰ {time_str} - Halfway point! How's your solution looking?")
            elif remaining == 300:  # 5 minutes left
                print(f"\n⚠️  {time_str} - 5 minutes left! Time to wrap up!")
            elif remaining == 60:   # 1 minute left
                print(f"\n🚨 {time_str} - 1 MINUTE LEFT!")
            elif remaining <= 10:   # Final countdown
                print(f"\r⏰ {time_str} ", end="", flush=True)
            else:
                print(f"\r⏰ {time_str} ", end="", flush=True)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print(f"\n\n⏹️  Timer stopped manually")
        elapsed = (datetime.now() - start_time).total_seconds()
        print(f"Time elapsed: {display_time(int(elapsed))}")
        return
    
    print(f"\n\n🎉 TIME'S UP! 🎉")
    print("=" * 50)
    print("Great job staying focused!")
    print("\n📝 Self-evaluation:")
    print("  - Did you solve the problem?")
    print("  - Can you explain your solution?")
    print("  - What would you do differently?")
    print("  - Which pattern did you use?")
    print("=" * 50)

def main():
    parser = argparse.ArgumentParser(description="Interview Practice Timer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--easy", action="store_true", help="15 minute timer for easy problems")
    group.add_argument("--medium", action="store_true", help="25 minute timer for medium problems")
    group.add_argument("--hard", action="store_true", help="35 minute timer for hard problems")
    group.add_argument("--custom", type=int, metavar="MINUTES", help="Custom timer in minutes")
    
    args = parser.parse_args()
    
    if args.easy:
        practice_timer(15, "Easy")
    elif args.medium:
        practice_timer(25, "Medium")
    elif args.hard:
        practice_timer(35, "Hard")
    elif args.custom:
        if args.custom <= 0:
            print("❌ Timer duration must be positive!")
            sys.exit(1)
        practice_timer(args.custom, "Custom")

if __name__ == "__main__":
    main() 