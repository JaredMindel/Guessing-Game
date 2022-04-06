##### Part 2 #####

word = "Google"
guesses_left = 7

while guesses_left > 0:
    guess = input("Guess the word")
    if len(guess) == 1: # The guess is a letter here
        if guess in word:
            if word.count(guess) == 1:
                print(word.index(guess) + 1) #show the location of the letter; I added 1 because Python indexes at 0
            else:
                for letter in word:
                    if guess == letter:
                        print(word[letter])
        else:
            print("That letter is not in the word")
            guesses_left = guesses_left - 1
            print("you have " + str(guesses_left) + " guesses left.")
    else: # The guess is a full word
        if guess == word:
            print("Hooray!")
            break
        else:
            print("Incorrect")
            guesses_left = guesses_left - 1
            print("you have " + str(guesses_left) + " guesses left.")

print("Hey")