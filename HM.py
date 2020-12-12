# Hangman Beginner project
import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list: words.py
    while '-' in word or ' ' in word: 
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    # Getting User input
    while len(word_letters) > 0:
        # Letters used
        # ' '.join(['a', 'b', 'c']) --> 'a', 'b', 'c'
        print('You have used these letters ' , ' '.join(used_letters))
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        
        else:
            print ('Invalid character. Please try again.')
    
    # Gets here when len(word_letters) == 0

user_input = input ('Type something: ')
print (user_input)