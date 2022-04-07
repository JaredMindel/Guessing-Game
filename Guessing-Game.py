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
    item = item.replace('"','')
    item = item.replace(' ', "")
    word_list.append(item)
words_dictionary.close()

record_dictionary = {}
record_dictionary['Wins'] = 0
record_dictionary['Losses'] = 0
record_dictionary['Previous Words'] = []

listed_word = ""
word = random.choice(word_list).lower()
for quantity in word:
        listed_word = listed_word + "_"
guess_list = []

def game():

    guesses_left = 7

    global word
    global word_list
    global listed_word
    global guess_list
    
    while guesses_left > 0:
        try:
            guess = (input("Make a guess").lower())
            if not guess.isalpha():
                print("Please, enter a string.")
                continue
            if guess in guess_list:
                print("You already guessed this")
                continue
            elif guess not in guess_list:
                guess_list.append(guess)
            if len(guess) == 1: # The guess is a letter here
                if guess in word:
                    for letter_spot in range(len(word)):
                        if(word[letter_spot] == guess):
                            listed_word = list(listed_word)
                            listed_word[letter_spot] = word[letter_spot]
                    if listed_word == list(word):
                        record_dictionary['Wins'] += 1
                        print('Hooray! You Won!')
                        if input("would you like to play again? Y/N").upper() == "Y":
                            record_dictionary['Previous Words'].append(word)
                            word_list.remove(word)
                            print(record_dictionary)
                            listed_word = ""
                            word = random.choice(word_list).lower()
                            for quantity in word:
                                listed_word = listed_word + "_"
                            game()
                        else:
                            break
                    else:
                        print(" ".join(listed_word))
                else:
                    print("That letter is not in the word")
                    guesses_left = guesses_left - 1
                    print("you have " + str(guesses_left) + " guesses left.") #show how many guesses are left
                    if guesses_left == 0:
                        record_dictionary['Losses'] += 1
                        if input("You lost! Would you like to play again? Y/N").upper() == "Y":
                            record_dictionary['Previous Words'].append(word)
                            word_list.remove(word)
                            print(record_dictionary)
                            listed_word = ""
                            word = random.choice(word_list).lower()
                            for quantity in word:
                                listed_word = listed_word + "_"
                            guess_list = []
                            game()
                        else:
                            break
            else: # The guess is a full word here
                if guess == word:
                    record_dictionary['Wins'] += 1
                    print("Hooray! You Won!")
                    if input("Would you like to play again? Y/N").upper() == "Y":
                        record_dictionary['Previous Words'].append(word)
                        word_list.remove(word)
                        listed_word = ""
                        word = random.choice(word_list).lower()
                        for quantity in word:
                            listed_word = listed_word + "_"
                        game()
                        break
                    else: 
                        break
                else:
                    print("Incorrect")
                    guesses_left = guesses_left - 1
                    print("you have " + str(guesses_left) + " guesses left.") #show how many guesses are left
                    if guesses_left == 0:
                        record_dictionary['Losses'] += 1
                        if input("You lost! Would you like to play again? Y/N").upper() == "Y":
                            record_dictionary['Previous Words'].append(word)
                            word_list.remove(word)
                            listed_word = ""
                            word = random.choice(word_list).lower()
                            for quantity in word:
                                listed_word = listed_word + "_"
                            print(record_dictionary)
                            game()
                        else:
                            break
        except ValueError:
            print("Input needs to be a string")
game()

