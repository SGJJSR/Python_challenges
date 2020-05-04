# Hangman game:

import string
import random
import numpy as np

def scribble_word(list_of_words):
    random_word = (random.choice(list_of_words).strip())
    return(random_word)
    
# sowpods is a list of all possible Scrabble words in English: 
with open('sowpods.txt', 'r') as f:  
lines = f.readlines()

# You die when you have more guesses wrong than there are letters in the word 
def hang():
    word = list(scribble_word(lines))
    print(word)
    n = len(word)
    play = np.empty(n, dtype = str)
    lives = n+1
    while lives > 0:
        z = str(input("Tell me a letter (in capitals) \n"))
        word_iter = iter(word)
        if z in word:
            while z in word:
                j = word.index(z)
                play[j] = z
                word[j] = ""
                print(play)
                if not '' in play:
                    return(print("Congrats! You won."))
        else:
            lives -= 1
            print("Remaining lives: {}".format(lives))
            if lives == 0 :
                  return(print("Sry! You lost."))
    print(play)
        
