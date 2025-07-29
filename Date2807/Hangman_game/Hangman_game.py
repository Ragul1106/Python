import random
from functools import wraps
from typing import List, Generator

class Hangman:
    def __init__(self, word_list_file: str = "words.txt", max_attempts: int = 6):
        self.word_list_file = word_list_file
        self.max_attempts = max_attempts
        self.word = ""
        self.attempts_left = max_attempts
        self.guessed_letters: List[str] = []
        self.load_words()
        self.select_random_word()
    
    def load_words(self) -> None:
        """File handling: Load words from a text file"""
        try:
            with open(self.word_list_file, 'r') as file:
                self.words = [word.strip().lower() for word in file.readlines() if word.strip().isalpha()]
        except FileNotFoundError:
            print(f"Warning: {self.word_list_file} not found. Using default word list.")
            self.words = ["python", "hangman", "programming", "computer", "keyboard", "developer"]
    
    def select_random_word(self) -> None:
        """Select a random word from the loaded words"""
        if not self.words:
            raise ValueError("No words available to play Hangman.")
        self.word = random.choice(self.words)
        self.attempts_left = self.max_attempts
        self.guessed_letters = []
    
    def display_word(self) -> str:
        """String operations: Display word with blanks (e.g., _ _ _ _)"""
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def guess_letter(self, letter: str) -> bool:
        """Conditionals: Check if letter is in word"""
        letter = letter.lower()
        if letter in self.guessed_letters:
            raise ValueError(f"You've already guessed '{letter}'")
        
        self.guessed_letters.append(letter)
        
        if letter in self.word:
            return True
        else:
            self.attempts_left -= 1
            return False
    
    def is_word_guessed(self) -> bool:
        """Check if the entire word has been guessed"""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def get_hint(self) -> Generator[str, None, None]:
        """Generator: Yield hints after 3 failed attempts"""
        unguessed_letters = [letter for letter in self.word if letter not in self.guessed_letters]
        if unguessed_letters and self.attempts_left <= self.max_attempts - 3:
            yield f"Hint: The word contains the letter '{random.choice(unguessed_letters)}'"
        else:
            yield "No hints available yet"
    
    def game_status(self) -> str:
        """Return current game status"""
        if self.is_word_guessed():
            return f"Congratulations! You guessed the word: {self.word}"
        elif self.attempts_left <= 0:
            return f"Game over! The word was: {self.word}"
        else:
            return f"Attempts left: {self.attempts_left} | Guessed letters: {', '.join(sorted(self.guessed_letters))}"

def validate_input(func):
    """Decorator: Validate letter guesses (single alphabet character)"""
    @wraps(func)
    def wrapper(self, letter: str):
        if not letter.isalpha() or len(letter) != 1:
            raise ValueError("Please enter a single alphabet character")
        return func(self, letter)
    return wrapper

class HangmanGame:
    def __init__(self):
        self.game = Hangman()
    
    def play(self) -> None:
        """Main game loop"""
        print("Welcome to Hangman!")
        print(f"Guess the word: {self.game.display_word()}")
        
        while True:
            # Check game status
            status = self.game.game_status()
            print(status)
            
            if "Congratulations" in status or "Game over" in status:
                break
            
            # Get player input
            try:
                letter = input("Guess a letter: ")
                self.process_guess(letter)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
            
            # Display current state
            print(f"\nWord: {self.game.display_word()}")
            
            # Offer hint if appropriate
            if self.game.attempts_left <= self.game.max_attempts - 3:
                hint = next(self.game.get_hint())
                print(hint)
        
        self.play_again()
    
    @validate_input
    def process_guess(self, letter: str) -> None:
        """Process a letter guess with validation"""
        correct = self.game.guess_letter(letter)
        if correct:
            print(f"Correct! '{letter}' is in the word.")
        else:
            print(f"Sorry, '{letter}' is not in the word.")
    
    def play_again(self) -> None:
        """Ask if player wants to play again"""
        choice = input("Would you like to play again? (y/n): ").lower()
        if choice == 'y':
            self.game.select_random_word()
            print(f"\nNew word: {self.game.display_word()}")
            self.play()
        else:
            print("Thanks for playing!")

# Example usage
if __name__ == "__main__":
    # Create a words.txt file if it doesn't exist
    try:
        with open("words.txt", "x") as f:
            f.write("python\nhangman\nprogramming\ncomputer\nkeyboard\ndeveloper\nalgorithm\nfunction\nvariable")
    except FileExistsError:
        pass
    
    # Start the game
    hangman = HangmanGame()
    hangman.play()