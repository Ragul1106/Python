def encode(message):
    return ' '.join(str(ord(c)) for c in message)

def decode(code):
    return ''.join(chr(int(c)) for c in code.split())

while True:
    print("\n1. Encode\n2. Decode\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        message = input("Enter message to encode: ")
        print("Encoded:", encode(message))
    elif choice == '2':
        code = input("Enter code to decode: ")
        print("Decoded:", decode(code))
    elif choice == '3':
        break
    else:
        print("Invalid choice")