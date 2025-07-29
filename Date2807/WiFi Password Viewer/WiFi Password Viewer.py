import subprocess
import re

def get_wifi_passwords():
    try:
        profiles_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='utf-8')
        profiles = re.findall(r"All User Profile\s*:\s(.*)", profiles_data)

        for profile in profiles:
            profile = profile.strip()
            try:
                password_data = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"], encoding='utf-8', stderr=subprocess.DEVNULL)
                password = re.search(r"Key Content\s*:\s(.*)", password_data)
                yield (profile, password.group(1) if password else "(No password)")
            except subprocess.CalledProcessError:
                yield (profile, "(Access denied or profile error)")
    except Exception as e:
        print(f"Error: {e}")

def save_to_file(results, filename="wifi_passwords.txt"):
    try:
        with open(filename, "w", encoding='utf-8') as f:
            for name, pwd in results:
                f.write(f"SSID: {name}\nPassword: {pwd}\n\n")
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    print("Fetching saved WiFi networks and passwords...\n")
    passwords = list(get_wifi_passwords())  
    for ssid, pwd in passwords:
        print(f"SSID: {ssid}\nPassword: {pwd}\n")

    save_to_file(passwords)

if __name__ == "__main__":
    main()
