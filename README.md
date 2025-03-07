📝 Updated README: USB Key Logger 🔑📂
A Python-based keylogger that automatically detects a USB drive, logs keystrokes in real time, and saves them to usb_log.txt on the USB device.

🚀 Features
✅ Automatic USB Detection – Logs keystrokes only when a USB drive is detected.
✅ Real-Time Logging – Captures every keystroke immediately.
✅ Background Execution – Runs silently, without opening a visible window.
✅ Stealth Mode – Can be compiled into an EXE for hidden execution.
✅ Stores Logs on USB – Saves all keystrokes in usb_log.txt on the USB drive.

🛠️ Installation & Usage
1️⃣ Install Dependencies
Before running the script, install the required package:


pip install pynput
2️⃣ Prepare the USB Drive
Ensure the USB drive has the following files:

📂 USB Drive (E:\, F:\, etc.)
 ├── usb_log.txt   # Log file for storing captured keystrokes
 ├── keylogger.exe # Compiled EXE for silent execution (Optional)
 ├── keylogger.py  # Python script (If running as a script)
📝 Note: If usb_log.txt doesn’t exist, the script will create it automatically.

3️⃣ Running the Keylogger
Run as a Python Script:
python keylogger.py


Convert to EXE (Optional for Stealth Mode):
To create a standalone EXE that runs without requiring Python installed:
pyinstaller --onefile --noconsole keylogger.py
💡 After conversion: The EXE file will be in the dist/ folder. Move it to your USB drive for execution.

🛑 Stopping the Keylogger
If running as a Python script: Close the terminal (Ctrl + C).
If running as an EXE:
Open Task Manager (Ctrl + Shift + Esc), find keylogger.exe, and end the task.
OR use the command:
taskkill /IM keylogger.exe /F

Also any inputs of advancements are seriously appreciated

⚠️ Windows Defender & Antivirus Detection
🚨 Important: If you compile it to an EXE, Windows Defender may detect and remove it.

⚠️ Disclaimer
🚨 This project is for educational and ethical use only! Unauthorized use of keyloggers is illegal and can lead to serious consequences. Use it responsibly.
For EXE files, consider using obfuscation techniques (e.g., PyArmor).

