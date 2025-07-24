import logging
from datetime import datetime

logging.basicConfig(filename='login.log', level=logging.ERROR)

class LoginFailedError(Exception):
    pass

def login_system():
    correct_password = "secret123"
    attempts = 0
    
    while attempts < 3:
        try:
            password = input("Enter password: ")
            if password != correct_password:
                attempts += 1
                raise ValueError("Incorrect password")
            else:
                print("Login successful!")
                break
        except ValueError as e:
            logging.error(f"{datetime.now()}: Attempt {attempts} - {e}")
            print(f"{e}. Attempts left: {3 - attempts}")
    else:
        try:
            raise LoginFailedError("Maximum attempts reached")
        except LoginFailedError as e:
            logging.error(f"{datetime.now()}: {e}")
            print(e)

login_system()