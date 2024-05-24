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
        self.guess = guess.lower()
         # Create an if statement that checks if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")


    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter:") 
            if len(guess) > 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in guess_list():
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)    

    

