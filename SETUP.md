# Setup Guide for BCI Robotic Arm Project

## Prerequisites

1. **Emotiv EEG Headset** with dongle or Bluetooth connection
2. **Arduino Uno** (or compatible) with servo motors
3. **Python 3.7+** installed
4. **Arduino IDE** for uploading code to the board
5. **Node-RED** for the flow control

## Step 1: Environment Setup

### Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Create Environment File
Create a `.env` file in the project root with your Emotiv API credentials:

```bash
# Get these from https://www.emotiv.com/developer/
CLIENT_ID=your_app_client_id_here
CLIENT_SECRET=your_app_client_secret_here
```

## Step 2: Hardware Setup

### Arduino Connection
1. Connect Arduino to your computer via USB
2. Upload `Hardware/sketch_feb29a/RobotArm/RobotArm.ino` to the board
3. Note the port (COM3 on Windows, /dev/tty.usbmodem* on macOS)

### Servo Motor Connections
- **Wrist**: Pin 2
- **Pinky**: Pin 3  
- **Ring**: Pin 4
- **Middle**: Pin 5
- **Index**: Pin 6
- **Thumb**: Pin 7

## Step 3: Emotiv Setup

### Install Emotiv Software
1. Download and install Emotiv Launcher
2. Connect your headset
3. Create an account and get API credentials
4. Ensure headset has good contact quality

### Training Mental Commands
The system recognizes these commands:
- **neutral**: Baseline state (no action)
- **lift**: Grab action (closes fingers)

**Note**: This simplified system only trains these two essential commands. The 'neutral' command is required as a baseline for comparison, and 'lift' is the action command that triggers the robotic arm.

## Step 4: Running the System

### Training Mode (First Time)
```bash
python train.py
```
This will:
1. Connect to your Emotiv headset
2. Train the 'neutral' command first (baseline)
3. Train the 'lift' command (grab action)
4. Save the trained profile

### Live Mode (After Training)
```bash
python live.py
```
This will:
1. Load your trained profile
2. Stream real-time mental command data
3. Show when 'lift' command is detected
4. Indicate when the grab script would be triggered

### Node-RED Integration
1. Start Node-RED
2. Import the flow from `Node-red Flows/flows (3).json`
3. Update the Python script paths in the flow
4. The flow will automatically call `grab.py` when "lift" command is detected

## Step 5: Testing

### Test Arduino Communication
```bash
python Mental_Command_Scripts/grab.py
```
This should send command "1" to Arduino and receive confirmation.

### Test Mental Commands
1. Put on the headset
2. Focus on the mental imagery for each command
3. Check if the robotic arm responds correctly

### Test Complete System
```bash
python test_lift_only.py
```
This will verify your entire setup is configured correctly.

## Troubleshooting

### Common Issues

**"No module named 'cortex'"**
- Install dependencies: `pip install -r requirements.txt`

**"Serial connection error"**
- Check Arduino is connected and port is correct
- Ensure no other program is using the serial port
- Try different USB ports

**"Profile access denied"**
- Disconnect and reconnect the headset
- Check API credentials in `.env` file
- Ensure headset has good contact quality

**"No headset found"**
- Check headset is connected via dongle or Bluetooth
- Ensure Emotiv Launcher can see the headset
- Try restarting Emotiv services

**"Invalid Parameters" error**
- This was caused by the old system trying to handle multiple commands
- The simplified system only handles 'neutral' and 'lift'
- Run `python test_lift_only.py` to verify setup

### Port Detection
The scripts now auto-detect Arduino ports:
- **Windows**: COM1, COM2, COM3, etc.
- **macOS**: /dev/tty.usbmodem*, /dev/tty.usbserial*
- **Linux**: /dev/ttyUSB*, /dev/ttyACM*

## Architecture Overview

```
EEG Headset → Python Scripts → Node-RED → Arduino → Robotic Arm
     ↓              ↓           ↓         ↓         ↓
  Brainwaves → Mental Commands → Flow → Serial → Servos
```

**Simplified Flow:**
1. **Think "lift"** → EEG detects brainwave pattern
2. **Python processes** → Identifies 'lift' command
3. **Node-RED triggers** → Calls `grab.py` script
4. **Arduino receives** → Command "1" via serial
5. **Servos move** → Fingers close to grab

## Next Steps

1. **Train mental commands** using `train.py`
2. **Test live detection** with `live.py`
3. **Integrate with Node-RED** for automated control
4. **Calibrate servo positions** for optimal movement
5. **Test complete system** with `test_lift_only.py`

## Support

- Emotiv API Documentation: https://emotiv.gitbook.io/cortex-api/
- Node-RED Documentation: https://nodered.org/docs/
- Arduino Servo Library: https://www.arduino.cc/reference/en/libraries/servo/
