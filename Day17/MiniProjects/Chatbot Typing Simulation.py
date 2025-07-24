import time

def chatbot_simulator():
    message = ""
    while True:

        new_msg = yield message
        if new_msg:
            message = ""
            for char in new_msg:
                message += char
                yield message  
                time.sleep(0.05) 
            yield "MESSAGE_COMPLETE"

bot = chatbot_simulator()
next(bot)  
bot.send("Hello! How can I help you today?")
