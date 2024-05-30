# %%
import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # Select random word from list
        self.word_guessed = list('_' * len(self.word)) # Create a list of empty spaces of the random word
        self.num_letters = len(set(self.word)) # number of unique letters in word
        self.num_lives = num_lives # number of lives left, default 5 
        self.word_list = word_list # List of words to be selected from 
        self.list_of_guesses = list() # list of guesses that have been made
        
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()
         # Create an if statement that checks if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    
       
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter:") 
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break    

def play_game(word_list, num_lives=5):
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("you lost")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else: 
            game.num_lives == 0 and game.num_letters == 0
            print("Congratulations! You won!")
            break
    
word_list = ["apple", "pear", "mango"]

# Start the game
play_game(word_list)

# %%
