#!/usr/bin/env python3
"""
Quick Start Script for BCI Robotic Arm Project
This script will guide you through the setup process
"""

import os
import sys
import subprocess
import time

def print_header():
    print("=" * 60)
    print("BCI Robotic Arm - Quick Start Guide")
    print("=" * 60)

def check_python_version():
    """Check if Python version is compatible"""
    print("1. Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"✗ Python {version.major}.{version.minor} detected. Python 3.7+ required.")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\n2. Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        print("  Try running: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and is configured"""
    print("\n3. Checking environment configuration...")
    
    if not os.path.exists('.env'):
        print("✗ .env file not found")
        print("  Creating .env file template...")
        
        env_content = """# Emotiv API Credentials
# Get these from https://www.emotiv.com/developer/
CLIENT_ID=your_app_client_id_here
CLIENT_SECRET=your_app_client_secret_here
"""
        
        try:
            with open('.env', 'w') as f:
                f.write(env_content)
            print("✓ .env file created")
            print("  Please edit .env file with your actual credentials")
            return False
        except Exception as e:
            print(f"✗ Failed to create .env file: {e}")
            return False
    
    # Check if credentials are still placeholder values
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        
        if not client_id or client_id == 'your_app_client_id_here':
            print("✗ CLIENT_ID not configured")
            print("  Please edit .env file with your actual credentials")
            return False
        
        if not client_secret or client_secret == 'your_app_client_secret_here':
            print("✗ CLIENT_SECRET not configured")
            print("  Please edit .env file with your actual credentials")
            return False
        
        print("✓ Environment variables configured")
        return True
        
    except Exception as e:
        print(f"✗ Error reading .env file: {e}")
        return False

def check_arduino_connection():
    """Check if Arduino is connected"""
    print("\n4. Checking Arduino connection...")
    
    try:
        import serial
        import glob
        
        # Find potential Arduino ports
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
        
        # Try to connect
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
        
    except ImportError:
        print("✗ pyserial not installed")
        return False
    except Exception as e:
        print(f"✗ Arduino connection test failed: {e}")
        return False

def run_test_script():
    """Run the test script to verify everything works"""
    print("\n5. Running comprehensive tests...")
    
    if os.path.exists('test_setup.py'):
        try:
            result = subprocess.run([sys.executable, 'test_setup.py'], 
                                 capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
            return result.returncode == 0
        except Exception as e:
            print(f"✗ Failed to run test script: {e}")
            return False
    else:
        print("✗ test_setup.py not found")
        return False

def show_next_steps():
    """Show what to do next"""
    print("\n" + "=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    
    print("1. Configure Emotiv API Credentials:")
    print("   - Edit .env file with your CLIENT_ID and CLIENT_SECRET")
    print("   - Get credentials from: https://www.emotiv.com/developer/")
    
    print("\n2. Connect Hardware:")
    print("   - Connect Emotiv headset to your computer")
    print("   - Connect Arduino via USB")
    print("   - Upload RobotArm.ino to Arduino")
    
    print("\n3. Train Mental Commands:")
    print("   - Run: python train.py")
    print("   - Follow the training process for each command")
    
    print("\n4. Test Live Mode:")
    print("   - Run: python live.py")
    print("   - Verify mental commands are detected")
    
    print("\n5. Integrate with Node-RED:")
    print("   - Import the flow from Node-red Flows/")
    print("   - Update Python script paths")
    print("   - Test automated control")
    
    print("\n6. Test Arduino Control:")
    print("   - Run: python Mental_Command_Scripts/grab.py")
    print("   - Verify robotic arm responds")

def main():
    """Main quick start function"""
    print_header()
    
    checks = [
        check_python_version,
        install_dependencies,
        check_env_file,
        check_arduino_connection,
        run_test_script
    ]
    
    all_passed = True
    for check in checks:
        if not check():
            all_passed = False
            print("\nPress Enter to continue to next check...")
            input()
    
    if all_passed:
        print("\n🎉 All checks passed! Your setup is ready.")
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
    
    show_next_steps()
    
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()
