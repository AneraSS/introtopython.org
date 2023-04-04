# Write a terminal app that asks people for their favorite games.
# Your app should offer users the choice of:
# Seeing all current games that are stored.
# Entering a new game.
# If the game is already stored, don't store it. Inform the user that you know that game, and like it too.
# If the game is not already stored, store it and tell the user you are happy to learn about that game.
# Quit.
# Your app should store all games when the program quits, so that it remembers all the games the next time it runs.
# Bonus: Add a "stats" element in your title bar that shows how many games are currently stored.

import os
import pickle


### FUNCTIONS ###

def load_games():
    try:
        file_object = open("games.txt", "rb")
        games = pickle.load(file_object)
        file_object.close()
        return games
    except Exception as error:
        print(error)
        return []       #  If the file doesn't exist, it creates an empty list.


def get_game():
    game = input("What's your favorite game? ")
    return game


def add_game():
    new_game = get_game()
    if new_game in games:
        print("The game is already in the list!")
    else:
        games.append(new_game)
        print ("Game added! I am happy to learn about that game.")


def ask_user():
    print("\nPlease, choose:")
    print("[1] to see all currently stored games.")
    print("[2] to enter a new game.")
    print("[q] to quit.")
    answer = input("What would you like to do? ")
    return answer


def show_games():
    for game in games:
        print(f"- {game}")


def quit():
    # This function dumps the names into a file, and prints a quit message.
    try:
        file_object = open('games.txt', 'wb')
        pickle.dump(games, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these games.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these games.")
        print(e)

### MAIN PROGRAM ###

games = load_games()
choice = ""

while choice != "q":
    choice = ask_user()

    if choice == "1":
        show_games()
    elif choice == "2": # ako je if, ne radi! elif i onda radi!
        add_game()
    elif choice == "q":
        quit()
        print("Thanks for playing.")
    else:
        print("I don't understand your choice. Please, re-enter.")