#!/usr/bin/env python3
"""
Test script to verify the simplified lift-only BCI system
"""

import os
import sys
from dotenv import load_dotenv

def test_environment():
    """Test if environment variables are set"""
    print("Testing environment setup...")
    
    load_dotenv()
    
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    
    if not client_id or client_id == 'your_app_client_id_here':
        print("✗ CLIENT_ID not configured")
        return False
    
    if not client_secret or client_secret == 'your_app_client_secret_here':
        print("✗ CLIENT_SECRET not configured")
        return False
    
    print("✓ Environment variables configured")
    return True

def test_imports():
    """Test if required modules can be imported"""
    print("\nTesting imports...")
    
    try:
        import cortex
        from cortex import Cortex
        print("✓ cortex module imported successfully")
    except ImportError as e:
        print(f"✗ cortex module import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv imported successfully")
    except ImportError as e:
        print(f"✗ python-dotenv import failed: {e}")
        return False
    
    return True

def test_training_script():
    """Test if training script can be imported and configured"""
    print("\nTesting training script...")
    
    try:
        # Import the training class
        sys.path.append('.')
        from train import Train
        
        # Test configuration
        load_dotenv()
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        
        # Create instance (don't actually connect)
        t = Train(client_id, client_secret)
        print("✓ Training class created successfully")
        
        # Check actions
        expected_actions = ['neutral', 'lift']
        if hasattr(t, 'actions'):
            print(f"✓ Actions configured: {t.actions}")
        else:
            print("✗ Actions not configured")
            return False
            
        return True
        
    except Exception as e:
        print(f"✗ Training script test failed: {e}")
        return False

def test_live_script():
    """Test if live script can be imported and configured"""
    print("\nTesting live script...")
    
    try:
        # Import the live class
        sys.path.append('.')
        from live import LiveAdvance
        
        # Test configuration
        load_dotenv()
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        
        # Create instance (don't actually connect)
        l = LiveAdvance(client_id, client_secret)
        print("✓ Live class created successfully")
        
        return True
        
    except Exception as e:
        print(f"✗ Live script test failed: {e}")
        return False

def show_system_overview():
    """Show how the simplified system works"""
    print("\n" + "=" * 60)
    print("SIMPLIFIED LIFT-ONLY SYSTEM OVERVIEW")
    print("=" * 60)
    
    print("🎯 What This System Does:")
    print("  • Trains ONLY 'neutral' and 'lift' mental commands")
    print("  • 'neutral' = baseline state (no action)")
    print("  • 'lift' = grab action (closes robotic fingers)")
    print("  • When 'lift' detected → Node-RED calls grab.py → Arduino moves")
    
    print("\n📋 Training Process:")
    print("  1. Run: python train.py")
    print("  2. Train 'neutral' command (baseline)")
    print("  3. Train 'lift' command (grab action)")
    print("  4. Profile saved automatically")
    
    print("\n🚀 Live Operation:")
    print("  1. Run: python live.py")
    print("  2. System detects mental commands in real-time")
    print("  3. 'lift' command triggers grab action")
    print("  4. Node-RED flow calls grab.py automatically")
    
    print("\n🔧 Hardware Control:")
    print("  • grab.py sends '1' to Arduino")
    print("  • Arduino moves servos to close fingers")
    print("  • Robotic arm grasps objects")
    
    print("\n⚠️  Important Notes:")
    print("  • Only 'lift' command triggers action")
    print("  • 'neutral' is just for baseline comparison")
    print("  • No complex sensitivity settings")
    print("  • No multiple command handling")

def main():
    """Run all tests"""
    print("Lift-Only BCI System Test")
    print("=" * 40)
    
    tests = [
        test_environment,
        test_imports,
        test_training_script,
        test_live_script
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! Your lift-only system is ready.")
        show_system_overview()
        
        print("\n🎯 Next Steps:")
        print("1. Ensure Emotiv headset is connected")
        print("2. Run: python train.py")
        print("3. Train 'neutral' then 'lift' commands")
        print("4. Test with: python live.py")
        print("5. Verify Node-RED calls grab.py when 'lift' detected")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Create .env file with your Emotiv API credentials")
        print("- Install dependencies: pip install -r requirements.txt")
        print("- Check headset connection")

if __name__ == "__main__":
    main()
