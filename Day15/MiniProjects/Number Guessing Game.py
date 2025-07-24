import random
import logging

logging.basicConfig(filename='guessing_game.log', level=logging.ERROR)

class GameOverError(Exception):
    pass

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    
    try:
        while attempts < 5:
            try:
                guess = int(input("Guess the number (1-100): "))
                if guess < 1 or guess > 100:
                    raise ValueError("Number must be between 1 and 100")
                    
                attempts += 1
                
                if guess == secret:
                    print(f"Correct! You guessed it in {attempts} tries")
                    return
                elif guess < secret:
                    print("Too low!")
                else:
                    print("Too high!")
                    
            except ValueError as e:
                logging.error(f"Attempt {attempts + 1}: {e}")
                print(e)
                
        raise GameOverError(f"Game over! The number was {secret}")
        
    except GameOverError as e:
        logging.error(str(e))
        print(e)
    finally:
        print("Thanks for playing!")

guessing_game()