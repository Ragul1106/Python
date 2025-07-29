import winsound  
import time
import os

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

TRANSLATION_FILE = "morse_translations.txt"

def morse_generator(text):
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            yield MORSE_CODE_DICT[char]
        else:
            raise ValueError(f"❌ Invalid character '{char}' encountered.")

def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(700, 150)  
        elif symbol == '-':
            winsound.Beep(700, 400)  
        elif symbol == '/':
            time.sleep(0.6)          
        time.sleep(0.2)             

def text_to_morse(text):
    try:
        morse_gen = morse_generator(text)
        morse_code = ' '.join(morse_gen)
        print(f"\n🔤 Original: {text}")
        print(f"📡 Morse Code: {morse_code}")
        return morse_code
    except ValueError as e:
        print(e)
        return None

def save_translation(original, morse):
    try:
        with open(TRANSLATION_FILE, 'a') as f:
            f.write(f"{original} -> {morse}\n")
        print("✅ Translation saved.")
    except Exception as e:
        print(f"❌ Failed to save: {e}")

def view_translations():
    if not os.path.exists(TRANSLATION_FILE):
        print("⚠️ No translations saved yet.")
        return
    with open(TRANSLATION_FILE, 'r') as f:
        print("\n🗂️ Saved Translations:")
        print(f.read())

def main():
    while True:
        print("\n🔸 1. Translate to Morse")
        print("🔸 2. View Saved Translations")
        print("🔸 3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            text = input("\nEnter text to convert: ").strip()
            morse = text_to_morse(text)
            if morse:
                play = input("▶️ Play morse code? (y/n): ").lower()
                if play == 'y':
                    play_morse(morse)
                save_translation(text, morse)

        elif choice == '2':
            view_translations()

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
