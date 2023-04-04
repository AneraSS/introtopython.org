# Hangman
# If it's been a while since you played Hangman, play it with someone first.
# Play both sides, so you remember how it feels as a player and as the person making up the word.
# Write a terminal app that replicates Hangman.

import random
import os
import pickle

### FUNCTIONS ###


def display_title():
    os.system('cls')
    print("################################")
    print("#### You're playing hangman ####")
    print("################################")


def get_choice():
    print("\nEnter [1] to play Hangman. ")
    print("Enter [2] to add your word to the pool.")
    print("Enter [3] to see pool of words.")
    print("Enter [q] to quit game.")
    choice = input("What would you like to do? ")
    return choice


def load_words():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        file_object = open('words.txt', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []


def quit():
    # This function dumps the names into a file, and prints a quit message.
    try:
        file_object = open('words.txt', 'wb')
        pickle.dump(words, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these words.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these words.")
        print(e)


def hangman():
    # Initialize hangman
    # I know, this part is redundant, but I like it.
    guess_word = random.choice(words)
    print("\nCan you guess?")
    number_of_underscores = len(guess_word)
    print(number_of_underscores * " __")
    print(f"Number of letters: {len(guess_word)}")

    count_wrong_guess = 0  # counts number of wrong guesses
    bad_letters = []  # list of wrong letters
    good_letters = []  # list of good letters
    secret_word = "__"  # final result that the player sees
    game_round = 0  # number of played rounds, total: 8

    while (count_wrong_guess < 8) and ("__" in secret_word):
        # user chooses a letter
        guess_letter = input("\nGuess a letter: ")

        # pool of good or bad letters
        if guess_letter in guess_word:
            if guess_letter in good_letters:
                print("You tried it already, and it's in the Secret Word!")
            else:
                print(f"Nice! {guess_letter} is present in the Secret Word!")
                good_letters.append(guess_letter)
        else:
            if guess_letter in bad_letters:
                print(f"Hey, you tried it already, and it's not in the Secret Word!")
            else:
                print(f"Nope, {guess_letter} is not present in the Secret Word.")
                bad_letters.append(guess_letter)
                count_wrong_guess += 1
        game_round += 1

        # visualize the game
        secret_word = ""
        for letter in guess_word:
            if letter in good_letters:
                secret_word += letter
            else:
                secret_word += " __ "

        # show the player current status
        print("\nStatus:")
        print(secret_word)
        print(f"Bad letters: {bad_letters}")
        print(f"Good letters: {good_letters}")
        print(f"Hangman status: {count_wrong_guess}/8")
        print(f"Game count #{game_round}")

    if count_wrong_guess == 8:
        print("Uh-oh! Hangman done!")


def add_word():
    enter_word = input("Enter a word to be added to the pool: ")
    if enter_word in words:
        print("\nWe've got that word already.")
    else:
        words.append(enter_word)
        print(f" '{enter_word}' added to the pool of words; nice!")


def display_words():
    print(f"Here is our current pool of words: {words}")


### MAIN PROGRAM ###

words = load_words()

choice = ""
display_title()

while choice != "q":
    choice = get_choice()

    if choice == "1":
        print("\nLet's play hangman!")
        hangman()
    elif choice == "2":
        add_word()
    elif choice == "3":
        display_words()
    elif choice == "q":
        quit()
    else:
        print("\nCan you re-enter your choice? ")