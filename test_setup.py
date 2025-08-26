#!/usr/bin/env python3
"""
Test script to verify the BCI Robotic Arm setup
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import websocket
        print("✓ websocket-client imported successfully")
    except ImportError as e:
        print(f"✗ websocket-client import failed: {e}")
        return False
    
    try:
        import serial
        print("✓ pyserial imported successfully")
    except ImportError as e:
        print(f"✗ pyserial import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv imported successfully")
    except ImportError as e:
        print(f"✗ python-dotenv import failed: {e}")
        return False
    
    try:
        from pydispatch import Dispatcher
        print("✓ pydispatch imported successfully")
    except ImportError as e:
        print(f"✗ pydispatch import failed: {e}")
        return False
    
    return True

def test_cortex_module():
    """Test if the custom cortex module can be imported"""
    print("\nTesting cortex module...")
    
    try:
        import cortex
        from cortex import Cortex
        print("✓ cortex module imported successfully")
        return True
    except ImportError as e:
        print(f"✗ cortex module import failed: {e}")
        return False

def test_environment_file():
    """Test if .env file exists and has required variables"""
    print("\nTesting environment file...")
    
    env_file = '.env'
    if not os.path.exists(env_file):
        print("✗ .env file not found")
        print("  Please create a .env file with CLIENT_ID and CLIENT_SECRET")
        return False
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        
        if not client_id or client_id == 'your_app_client_id_here':
            print("✗ CLIENT_ID not set or still has placeholder value")
            return False
        
        if not client_secret or client_secret == 'your_app_client_secret_here':
            print("✗ CLIENT_SECRET not set or still has placeholder value")
            return False
        
        print("✓ .env file configured with API credentials")
        return True
        
    except Exception as e:
        print(f"✗ Error reading .env file: {e}")
        return False

def test_arduino_connection():
    """Test if Arduino can be detected"""
    print("\nTesting Arduino connection...")
    
    try:
        import serial
        import glob
        
        # Try to find Arduino ports
        if sys.platform.startswith('win'):
            ports = [f'COM{i}' for i in range(10)]
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.usbmodem*') + glob.glob('/dev/tty.usbserial*')
        else:
            ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
        
        if not ports:
            print("✗ No Arduino ports detected")
            print("  Please connect Arduino via USB")
            return False
        
        print(f"✓ Found potential Arduino ports: {ports}")
        
        # Try to connect to first available port
        for port in ports:
            try:
                ser = serial.Serial(port=port, baudrate=9600, timeout=1)
                ser.close()
                print(f"✓ Successfully connected to {port}")
                return True
            except:
                continue
        
        print("✗ Could not establish connection to any port")
        return False
        
    except Exception as e:
        print(f"✗ Arduino connection test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("BCI Robotic Arm Setup Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_cortex_module,
        test_environment_file,
        test_arduino_connection
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
        print("✓ All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Ensure Emotiv headset is connected")
        print("2. Run: python train.py")
        print("3. Follow the training process")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Install dependencies: pip install -r requirements.txt")
        print("- Create .env file with your Emotiv API credentials")
        print("- Connect Arduino via USB")
        print("- Check headset connection")

if __name__ == "__main__":
    main()
