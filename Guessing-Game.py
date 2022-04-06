##### Part 2 #####

word = "Google".lower()
listed_word = ""
new_word = ""
guesses_left = 7

for quantity in word:
    listed_word = listed_word + "_"

while guesses_left > 0:
    guess = input("Make a guess").lower()
    if len(guess) == 1: # The guess is a letter here
        if guess in word:
            for letter_spot in range(len(word)):
                if(word[letter_spot] == guess):
                    listed_word = list(listed_word)
                    listed_word[letter_spot] = word[letter_spot]
            if listed_word == list(word):
                print('Hooray! You Won!')
                break
            else:
                print(" ".join(listed_word))
        else:
            print("That letter is not in the word")
            guesses_left = guesses_left - 1
            print("you have " + str(guesses_left) + " guesses left.") #show how many guesses are left
    else: # The guess is a full word here
        if guess == word:
            print("Hooray! You Won!")
            break
        else:
            print("Incorrect")
            guesses_left = guesses_left - 1
            print("you have " + str(guesses_left) + " guesses left.") #show how many guesses are left
else: print("Game Over, you lost!")