import time

def typing_test():
    test_text = "The quick brown fox jumps over the lazy dog"
    print(f"Type this: '{test_text}'")
    
    start = time.time()
    user_input = input("Start typing: ")
    end = time.time()
    
    time_taken = end - start
    words = len(test_text.split())
    wpm = (words / time_taken) * 60
    
    correct = 0
    for i in range(min(len(test_text), len(user_input))):
        if test_text[i] == user_input[i]:
            correct += 1
    
    accuracy = (correct / len(test_text)) * 100
    
    print(f"\nTime: {time_taken:.2f} seconds")
    print(f"Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()