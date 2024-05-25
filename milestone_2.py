# %%
import random 

'''
This action defines a list of words
'''
# Define a word list of 5 fruits
word_list = ["Apple", "Banana", "Pear", "Plum", "Mango"]
# print(word_list) # retain for testing
'''
This object chooses one word from the word list
'''
# Randomly select one of the words from word list
word = random.choice(word_list)
# print(word) # Retain for testing
'''
This asks the user to guess a letter
'''
guess = input("Please enter a letter:")
'''
This statement checks the chosen input is a single letter
'''
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print("Oops! That is not valid input.")

# print('Letter choice:', guess) # retain for testing 

# %%
