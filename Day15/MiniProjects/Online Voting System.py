import logging
from datetime import datetime

logging.basicConfig(filename='voting.log', level=logging.ERROR)

class AlreadyVotedError(Exception):
    pass

def voting_system():
    voted_users = set()
    
    try:
        user_id = input("Enter your user ID: ")
        if user_id in voted_users:
            raise AlreadyVotedError("You have already voted")
            
        print("Candidates:")
        print("1. Alice")
        print("2. Bob")
        print("3. Charlie")
        
        choice = int(input("Enter your choice (1-3): "))
        if choice < 1 or choice > 3:
            raise ValueError("Invalid choice")
            
        voted_users.add(user_id)
        print("Vote recorded successfully")
        
    except AlreadyVotedError as e:
        logging.error(f"{datetime.now()}: {e}")
        print(e)
    except ValueError as e:
        logging.error(f"{datetime.now()}: Invalid input - {e}")
        print(e)
    except Exception as e:
        logging.error(f"{datetime.now()}: Unexpected error - {e}")
        print("An error occurred")
    finally:
        print("Thank you for participating")

voting_system()