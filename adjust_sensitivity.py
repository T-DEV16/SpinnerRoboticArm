#!/usr/bin/env python3
"""
Real-time sensitivity adjustment for the BCI system
Run this in a separate terminal while live.py is running
"""

import time
import os

def show_sensitivity_guide():
    """Show the sensitivity guide"""
    print("\n" + "=" * 60)
    print("POWER SENSITIVITY GUIDE")
    print("=" * 60)
    print("The power threshold controls how easily the 'lift' command triggers:")
    print()
    print("🔴 0.1-0.3: VERY SENSITIVE")
    print("   • Triggers with minimal mental effort")
    print("   • May trigger accidentally")
    print("   • Good for beginners or weak signals")
    print()
    print("🟡 0.4-0.6: MEDIUM SENSITIVE (RECOMMENDED)")
    print("   • Balanced sensitivity")
    print("   • Requires focused mental effort")
    print("   • Good for most users")
    print()
    print("🟢 0.7-0.9: LESS SENSITIVE")
    print("   • Requires strong mental focus")
    print("   • Less likely to trigger accidentally")
    print("   • Good for experienced users")
    print()
    print("⚪ 0.0: ALWAYS TRIGGER (for testing)")
    print("⚫ 1.0: NEVER TRIGGER (for testing)")
    print()

def get_current_threshold():
    """Get the current threshold from live.py if it's running"""
    try:
        # Try to read from a temporary file if live.py saves the threshold
        if os.path.exists('.current_threshold'):
            with open('.current_threshold', 'r') as f:
                return float(f.read().strip())
    except:
        pass
    return 0.5  # Default

def save_threshold(threshold):
    """Save the threshold to a file for live.py to read"""
    try:
        with open('.current_threshold', 'w') as f:
            f.write(str(threshold))
    except:
        pass

def main():
    """Main sensitivity adjustment interface"""
    print("🎯 BCI Power Sensitivity Adjuster")
    print("Run this while live.py is running to adjust sensitivity")
    
    show_sensitivity_guide()
    
    current_threshold = get_current_threshold()
    print(f"Current threshold: {current_threshold:.3f}")
    
    while True:
        print("\n" + "-" * 40)
        print("Options:")
        print("1. Set specific threshold (0.0-1.0)")
        print("2. Quick presets")
        print("3. Show current threshold")
        print("4. Show sensitivity guide")
        print("5. Exit")
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                try:
                    new_threshold = float(input("Enter new threshold (0.0-1.0): "))
                    if 0.0 <= new_threshold <= 1.0:
                        save_threshold(new_threshold)
                        print(f"✅ Threshold set to: {new_threshold:.3f}")
                        
                        if new_threshold < 0.3:
                            print("🔴 Very sensitive - may trigger easily!")
                        elif new_threshold < 0.6:
                            print("🟡 Medium sensitivity - balanced")
                        else:
                            print("🟢 Less sensitive - requires strong focus")
                    else:
                        print("❌ Threshold must be between 0.0 and 1.0")
                except ValueError:
                    print("❌ Please enter a valid number")
                    
            elif choice == '2':
                print("\nQuick Presets:")
                print("1. Very Sensitive (0.2)")
                print("2. Sensitive (0.4)")
                print("3. Balanced (0.6)")
                print("4. Less Sensitive (0.8)")
                print("5. Back to main menu")
                
                preset_choice = input("Choose preset (1-5): ").strip()
                
                presets = {
                    '1': 0.2,
                    '2': 0.4,
                    '3': 0.6,
                    '4': 0.8
                }
                
                if preset_choice in presets:
                    threshold = presets[preset_choice]
                    save_threshold(threshold)
                    print(f"✅ Threshold set to: {threshold:.3f}")
                elif preset_choice == '5':
                    continue
                else:
                    print("❌ Invalid choice")
                    
            elif choice == '3':
                current = get_current_threshold()
                print(f"Current threshold: {current:.3f}")
                
            elif choice == '4':
                show_sensitivity_guide()
                
            elif choice == '5':
                print("👋 Exiting sensitivity adjuster")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Exiting sensitivity adjuster")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
