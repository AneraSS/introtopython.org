import random

words = ["car", "hospital", "kids", "tv", "book", "countryside"]


def hangman():
    # Initialize hangman
    guess_word = random.choice(words)
    print("\nCan you guess?")
    number_of_underscores = len(guess_word)
    print(number_of_underscores * " __")
    print(f"Number of letters: {len(guess_word)}")

    count_wrong_guess = 0  # counts number of wrong guesses
    bad_letters = []  # list of wrong letters
    good_letters = []   # list of good letters
    secret_word = "__"  # final result that the player sees
    game_round = 0  # number of played rounds, total: 8

    while (count_wrong_guess < 9) and ("__" in secret_word):
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


hangman()
