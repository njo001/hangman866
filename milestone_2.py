
import random 

# %%
# Define a word list of 5 fruits
word_list = ["Apple", "Banana", "Pear", "Plum", "Mango"]
print(word_list)

# Randomly select one of the words from word list
word = random.choice(word_list)
print(word)

guess = input("Please enter a letter:")
print(guess)

# %%
