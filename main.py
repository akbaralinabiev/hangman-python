import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word
def hangman():
    word = get_valid_word(words)
    word_letters = set(word.upper())
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 10 

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives , " lives and used these letters are stored here: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word.upper()]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already guessed that charachter. Try again.")
        else:
            print("Invalid charachter. Please try again.")
            

    # Game ends
    if lives == 0:
        print("Sorry, you died :( the word was ", word)
    else:
        print("Congratulations! You guessed the word '", word ,"' correctly!")

hangman()
