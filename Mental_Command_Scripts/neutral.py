# Importing Libraries 
import serial
import time
import sys
import os

# Auto-detect port based on OS
def get_arduino_port():
    if sys.platform.startswith('win'):
        # Windows - try COM ports
        for i in range(10):
            try:
                port = f'COM{i}'
                test_serial = serial.Serial(port=port, baudrate=9600, timeout=1)
                test_serial.close()
                return port
            except:
                continue
    elif sys.platform.startswith('darwin'):
        # macOS - try /dev/tty.usbmodem* or /dev/tty.usbserial*
        import glob
        ports = glob.glob('/dev/tty.usbmodem*') + glob.glob('/dev/tty.usbserial*')
        if ports:
            return ports[0]
    else:
        # Linux - try /dev/ttyUSB* or /dev/ttyACM*
        import glob
        ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
        if ports:
            return ports[0]
    
    # Fallback
    return 'COM3' if sys.platform.startswith('win') else '/dev/tty.usbmodem*'

try:
    port = get_arduino_port()
    print(f"Connecting to Arduino on port: {port}")
    arduino = serial.Serial(port=port, baudrate=9600, timeout=1)
    
    while True:
        arduino.write('5'.encode('utf-8'))
        print("Sent reset command (5) to Arduino")

        try:
            boardData = arduino.readline().decode('ascii').strip()
            print(f"Arduino response: {boardData}")
        except UnicodeDecodeError:
            boardData = arduino.readline().decode('ascii', errors='ignore').strip()
            print(f"Arduino response (decoded with errors): {boardData}")
        
        if boardData == '5':
            print("Reset command confirmed by Arduino")
            break
        time.sleep(1)
        
except serial.SerialException as e:
    print(f"Serial connection error: {e}")
    print("Please check:")
    print("1. Arduino is connected via USB")
    print("2. Arduino IDE has the correct port selected")
    print("3. No other program is using the serial port")
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        arduino.close()
        print("Serial connection closed")
    except:
        pass
