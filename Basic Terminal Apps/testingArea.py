import random
import os

words = ["car", "hospital", "kids", "TV", "book", "countryside"]


def hangman():
    # Initialize hangman
    guess_word = random.choice(words)
    print("\nCan you guess?")
    number_of_underscores = len(guess_word)
    print(number_of_underscores * " __")
    print(f"\nNumber of letters: {len(guess_word)}")

    count_wrong_guess = 0  # counts number of wrong guesses
    bad_letters = []  # list of wrong letters
    secret_word = ""  # word that the player sees
    game_round = 0  # number of played rounds, total: 8

    while (game_round < 9) or (" __ " in secret_word):
        guess_letter = input("\nGuess a letter: ")

        if guess_letter in guess_word:
            print(f"Correct: #{guess_letter}!")
            for letter in guess_word:
                if letter == guess_letter:
                    secret_word += letter
                else:
                    secret_word += " __ "
        else:
            bad_letters.append(guess_letter)
            count_wrong_guess += 1

        print(secret_word)
        print(f"\nNumber of errors: {count_wrong_guess}/8")
        print(f"Tried letters: {bad_letters}")
        game_round += 1
        print(f"Round: {game_round}/8")


hangman()
