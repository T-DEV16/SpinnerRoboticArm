# Configuration Guide

## Environment Variables Setup

### 1. Create .env File
Create a `.env` file in the project root directory with the following content:

```bash
# Emotiv API Credentials
CLIENT_ID=your_actual_client_id_here
CLIENT_SECRET=your_actual_client_secret_here
```

### 2. Get Emotiv API Credentials

1. Go to [Emotiv Developer Portal](https://www.emotiv.com/developer/)
2. Sign up or log in to your account
3. Create a new application
4. Copy the `Client ID` and `Client Secret`
5. Replace the placeholder values in your `.env` file

### 3. Example .env File
```bash
CLIENT_ID=abc123def456ghi789
CLIENT_SECRET=xyz789uvw456rst123
```

## Profile Configuration

### Default Profile Name
The scripts use `'TRAW spins'` as the default profile name. You can change this in:

- `train.py` line 280: `profile_name = 'TRAW spins'`
- `live.py` line 285: `trained_profile_name = 'TRAW spins'`

### Mental Commands
The system is configured to train these commands:
- `neutral` - Baseline state
- `lift` - Grab action (closes fingers)

You can modify the actions list in `train.py` line 281:
```python
actions = ['neutral', 'lift', 'drop', 'left', 'right']
```

## Arduino Configuration

### Port Settings
- **Baudrate**: 9600 (matches Arduino sketch)
- **Port**: Auto-detected for your OS
  - Windows: COM1, COM2, COM3, etc.
  - macOS: /dev/tty.usbmodem*, /dev/tty.usbserial*
  - Linux: /dev/ttyUSB*, /dev/ttyACM*

### Servo Pin Mapping
```cpp
// Arduino pin assignments
wrist.attach(2);   // Wrist rotation
pinky.attach(3);   // Pinky finger
ring.attach(4);    // Ring finger
middle.attach(5);  // Middle finger
index.attach(6);   // Index finger
thumb.attach(7);   // Thumb
```

## Node-RED Configuration

### Flow Import
1. Import the flow from `Node-red Flows/flows (3).json`
2. Update Python script paths to match your system:
   - `grab.py`: `/path/to/your/project/Mental_Command_Scripts/grab.py`
   - `neutral.py`: `/path/to/your/project/Mental_Command_Scripts/neutral.py`

### Profile Name
Ensure the profile name in Node-RED matches your trained profile:
- Default: `TRAW spins`
- Update in the "Profile Name" node

## Testing Configuration

### Run Setup Test
```bash
python test_setup.py
```

This will verify:
- All dependencies are installed
- Environment variables are set
- Arduino connection works
- Cortex module loads correctly

### Manual Testing
1. **Arduino**: `python Mental_Command_Scripts/grab.py`
2. **Training**: `python train.py`
3. **Live Mode**: `python live.py`

## Troubleshooting Configuration

### Common Issues

**"CLIENT_ID not set"**
- Check `.env` file exists in project root
- Verify no spaces around `=` in `.env` file
- Ensure file is not saved with `.txt` extension

**"Arduino port not found"**
- Check USB connection
- Try different USB ports
- Verify Arduino IDE shows the correct port
- Restart Arduino IDE if needed

**"Profile not found"**
- Ensure profile name matches exactly (case-sensitive)
- Check if profile was saved after training
- Try creating a new profile with a different name

### Environment File Location
The `.env` file must be in the same directory as `train.py` and `live.py`:
```
RoboticArm/
├── .env              ← Create this file here
├── train.py
├── live.py
├── cortex.py
└── ...
```
