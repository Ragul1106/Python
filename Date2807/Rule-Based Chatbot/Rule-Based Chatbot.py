import json
from functools import wraps
from typing import Dict, List, Generator
from datetime import datetime

class Chatbot:
    def __init__(self, responses_file: str = "responses.json"):
        self.responses_file = responses_file
        self.responses: Dict[str, str] = {}
        self.load_responses()
        self.chat_log: List[Dict[str, str]] = []
    
    def load_responses(self) -> None:
        """File handling: Load responses from JSON"""
        try:
            with open(self.responses_file, 'r') as file:
                self.responses = json.load(file)
        except FileNotFoundError:
            print(f"Warning: {self.responses_file} not found. Using default responses.")
            self.responses = {
                "hi": "Hello! How can I help you today?",
                "hello": "Hi there! What can I do for you?",
                "bye": "Goodbye! Have a great day!",
                "exit": "Goodbye! Come back if you have more questions.",
                "help": "I can answer questions about our products, services, and policies. Try asking about shipping, returns, or pricing.",
                "shipping": "We offer free shipping on orders over $50. Standard shipping takes 3-5 business days.",
                "returns": "You can return items within 30 days of purchase. Please contact customer service for a return authorization.",
                "pricing": "Our pricing is competitive. For specific product prices, please visit our website or ask about a particular item.",
                "hours": "Our customer service is available Monday to Friday, 9am to 5pm."
            }
        except json.JSONDecodeError:
            print(f"Error: {self.responses_file} contains invalid JSON. Using default responses.")
            self.responses = {
                "hi": "Hello! How can I help you today?",
                "hello": "Hi there! What can I do for you?"
            }
    
    def save_responses(self) -> None:
        """Save responses to JSON file"""
        with open(self.responses_file, 'w') as file:
            json.dump(self.responses, file, indent=4)
    
    def find_best_match(self, query: str) -> Generator[str, None, None]:
        """Generator: Yield possible responses based on keyword matching"""
        query_lower = query.lower()
        for keyword, response in self.responses.items():
            if keyword in query_lower:
                yield response
    
    def get_response(self, query: str) -> str:
        """Get chatbot response with case-insensitive matching"""
        if not query.strip():
            return "Please type something so I can help you."

        query_lower = query.lower()
        if query_lower in self.responses:
            return self.responses[query_lower]

        possible_responses = list(self.find_best_match(query))
        if possible_responses:
            return possible_responses[0]  

        return "I'm not sure I understand. Could you rephrase your question or try asking about something else?"
    
    @log_chat
    def chat(self) -> None:
        """Main chat loop"""
        print("Chatbot: Hello! I'm your helpful assistant. Type 'exit' to end the conversation.")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['exit', 'bye', 'quit']:
                    print(f"Chatbot: {self.responses.get('exit', 'Goodbye!')}")
                    break
                
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except KeyboardInterrupt:
                print("\nChatbot: Goodbye!")
                break
            except Exception as e:
                print(f"Chatbot: Sorry, something went wrong. Please try again. ({str(e)})")

def log_chat(func):
    """Decorator: Save conversations to a log file"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):

        self.chat_log.append({
            "timestamp": datetime.now().isoformat(),
            "event": "Conversation started"
        })

        result = func(self, *args, **kwargs)

        self.chat_log.append({
            "timestamp": datetime.now().isoformat(),
            "event": "Conversation ended"
        })

        self.save_chat_log()
        
        return result
    return wrapper

    def save_chat_log(self) -> None:
        """Save chat log to file"""
        try:
            with open("chat_log.json", 'a') as file:
                for entry in self.chat_log:
                    json.dump(entry, file)
                    file.write("\n")
            self.chat_log = []  
        except IOError as e:
            print(f"Warning: Could not save chat log. {str(e)}")
    
    def add_response(self, keyword: str, response: str) -> None:
        """Add a new response to the chatbot's knowledge base"""
        self.responses[keyword.lower()] = response
        self.save_responses()
        print(f"Added new response for '{keyword}'")

if __name__ == "__main__":

    bot = Chatbot()

    bot.chat()
