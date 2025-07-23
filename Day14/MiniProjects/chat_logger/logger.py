import os
from datetime import datetime
import time

LOG_DIR = "chat_logs"
os.makedirs(LOG_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(LOG_DIR, f"session_log_{timestamp}.txt")

SAVE_INTERVAL = 120  

chat_history = []

def log_message(sender, message):
    entry = f"[{datetime.now().strftime('%H:%M:%S')}] {sender}: {message}"
    print(entry)
    chat_history.append(entry)

def save_log():
    with open(log_file_path, "w", encoding='utf-8') as f:
        for line in chat_history:
            f.write(line + "\n")
    print("💾 Log saved.")

def chat_session():
    print("💬 Chat Logger Started. Type 'exit' to end chat.")
    admin_mode = input("Login as admin? (y/n): ").strip().lower() == 'y'

    last_save_time = time.time()
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() == "exit":
            break
        if admin_mode and user_msg.startswith("delete log"):
            if os.path.exists(log_file_path):
                os.remove(log_file_path)
                print("🗑️ Chat log deleted by admin.")
                chat_history.clear()
            continue

        log_message("You", user_msg)

        bot_response = "This is a placeholder bot reply."  
        log_message("Bot", bot_response)

        if time.time() - last_save_time > SAVE_INTERVAL:
            save_log()
            last_save_time = time.time()

    save_log()
    print("👋 Chat ended and saved.")

if __name__ == "__main__":
    chat_session()
