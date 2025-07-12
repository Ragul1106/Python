responses = {
    "hi": "Hello! How can I help you?",
    "name": "I'm a simple chatbot",
    "bye": "Goodbye! Have a nice day!"
}

def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print("Chatbot:", responses["bye"])
            break
        
        response = responses.get(user_input, "I didn't understand that")
        print("Chatbot:", response)

chatbot()