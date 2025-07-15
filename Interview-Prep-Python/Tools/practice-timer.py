#!/usr/bin/env python3
"""
Python Interview Practice Timer

A simple tool to help time your Python coding practice sessions.
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
from typing import Optional


def display_time(seconds: int) -> str:
    """Convert seconds to MM:SS format"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


def practice_timer(duration_minutes: int, problem_type: str = "Custom") -> None:
    """Run a practice timer with motivational messages"""
    total_seconds = duration_minutes * 60
    
    print(f"\n🐍 {problem_type} Python Problem Timer: {duration_minutes} minutes")
    print("=" * 50)
    print("💡 Python Interview Tips:")
    print("  1. Think about which collections to use")
    print("  2. Consider list comprehensions for clean code")
    print("  3. Use type hints for clarity")
    print("  4. Start with Pythonic solution, then optimize")
    print("  5. Test with edge cases")
    print("=" * 50)
    
    input("\n⏱️  Press ENTER to start timer...")
    
    start_time = datetime.now()
    print(f"\n🚀 Python timer started at {start_time.strftime('%H:%M:%S')}")
    print("Focus mode: ON! Code Pythonically! 🐍\n")
    
    try:
        for remaining in range(total_seconds, 0, -1):
            time_str = display_time(remaining)
            
            # Motivational checkpoints
            if remaining == total_seconds // 2:
                print(f"\n⏰ {time_str} - Halfway point! Is your solution Pythonic?")
            elif remaining == 300:  # 5 minutes left
                print(f"\n⚠️  {time_str} - 5 minutes left! Time to add type hints!")
            elif remaining == 60:   # 1 minute left
                print(f"\n🚨 {time_str} - 1 MINUTE LEFT! Final cleanup!")
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
    
    print(f"\n\n🎉 TIME'S UP! Great Python coding! 🎉")
    print("=" * 50)
    print("Excellent work staying focused!")
    print("\n📝 Python Self-evaluation:")
    print("  - Did you solve the problem?")
    print("  - Is your solution Pythonic?")
    print("  - Did you use appropriate collections?")
    print("  - Are there type hints and docstrings?")
    print("  - What Python pattern did you use?")
    print("  - How would you optimize further?")
    print("=" * 50)


def main() -> None:
    parser = argparse.ArgumentParser(description="Python Interview Practice Timer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--easy", action="store_true", 
                      help="15 minute timer for easy Python problems")
    group.add_argument("--medium", action="store_true", 
                      help="25 minute timer for medium Python problems")
    group.add_argument("--hard", action="store_true", 
                      help="35 minute timer for hard Python problems")
    group.add_argument("--custom", type=int, metavar="MINUTES", 
                      help="Custom timer in minutes")
    
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