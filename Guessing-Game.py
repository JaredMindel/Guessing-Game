##### Part 2 #####
import os
import json
import random

os.chdir(r'C:\Users\jared\Dev-10 Module Exercises\Python\Python Basics\Guessing Game\english-words-master')
print(os.getcwd())

words_dictionary = open(r'words_dictionary.json')
dictionary_lines = words_dictionary.read().splitlines()

word_list = []

for item in dictionary_lines:
    item = item.split(":")
    item = item[0]
    word_list.append(item)
words_dictionary.close()

listed_word = ""
new_word = ""
guesses_left = 7
record_dictionary = {}
record_dictionary['Wins'] = 0
record_dictionary['Losses'] = 0
record_dictionary['Previous Words'] = []

continue_attempt = "N"

word_list = ['test', 'brian']

word = random.choice(word_list).lower()
for quantity in word:
        listed_word = listed_word + "_"

def game():
    
    global guesses_left
    global word
    global word_list
    global listed_word
    global continue_attempt

    while guesses_left > 0:
        global continue_attempt
        if continue_attempt == "Y":
            listed_word = ""
            if word in record_dictionary['Previous Words']:
                word_list.remove(word)
            word = random.choice(word_list).lower()
            for quantity in word:
                listed_word = listed_word + "_"
            continue_attempt = 'N'
            continue
        guess = input("Make a guess").lower()
        if len(guess) == 1: # The guess is a letter here
            if guess in word:
                for letter_spot in range(len(word)):
                    if(word[letter_spot] == guess):
                        listed_word = list(listed_word)
                        listed_word[letter_spot] = word[letter_spot]
                if listed_word == list(word):
                    print('Hooray! You Won!')
                    if input("would you like to play again? Y/N").upper() == "Y":
                        record_dictionary['Previous Words'].append(word)
                        print(record_dictionary)
                        continue_attempt = "Y"
                        break
                    else:
                        break
                else:
                    print(" ".join(listed_word))
            else:
                print("That letter is not in the word")
                guesses_left = guesses_left - 1
                print("you have " + str(guesses_left) + " guesses left.") #show how many guesses are left
                if guesses_left == 0:
                    if input("You lost! Would you like to play again? Y/N").upper() == "Y":
                        record_dictionary['Previous Words'].append(word)
                        print(record_dictionary)
                        continue_attempt = "Y"
                        continue
                    else:
                        break
        else: # The guess is a full word here
            if guess == word:
                print("Hooray! You Won!")
                if input("Would you like to play again? Y/N").upper() == "Y":
                    record_dictionary['Previous Words'].append(word)
                    continue
                else: 
                    break
            else:
                print("Incorrect")
                guesses_left = guesses_left - 1
                print("you have " + str(guesses_left) + " guesses left.") #show how many guesses are left
                if guesses_left == 0:
                    if input("You lost! Would you like to play again? Y/N").upper() == "Y":
                        record_dictionary['Previous Words'].append(word)
                        print(record_dictionary)
                        game()
                    else:
                        break
game()

if continue_attempt.upper() == "Y":
    guesses_left = 7
    game()