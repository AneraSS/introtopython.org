import os
import pickle
import random

#### FUNCTIONS ####

def display_title():
    os.system('cls')
    print("************************************************************************************************************")
    print("***************************** W O R L D   W A L L **********************************************************")
    print("* A word wall is a place on your wall where you keep track of the new words and meanings you are learning. *")
    print("************************************************************************************************************")


def see_dict():
    print("\nHere are all words and meanings entered thus far:")
    for name, meaning in world_wall.items():
        if meaning['category'] == None:
            print(f"- {name.title()} means {meaning['description']}.")
        else:
            print(f"- {name.title()} means {meaning['description']}, and is a {meaning['category']}.")


def get_choice():
    print("\nEnter [1] to see all words and meanings entered thus far.")
    print("Enter [2] to enter new word-meaning pair.")
    print("Enter [3] to categorize your words.")
    print("Enter [4] to correct the spelling of a word.")
    print("Enter [5] to play the quiz game where you guess the word based on description.")
    print("Enter [q] to quit.")
    return input()


def load_world_wall():
    # loads from file and puts them in dict "world_wall
    # if doesn't exist, creates an empty one
    try:
        file_object = open(datafile, "rb")
        world_wall = pickle.load(file_object)
        file_object.close()
        return world_wall
    except Exception as e:
        print(e)
        return {}


def quit():
    # dumps into a file, and prints the quit message
    try:
        file_object = open(datafile, "wb")
        pickle.dump(world_wall, file_object)
        file_object.close()
        print("\nThanks for using the World Wall. I'll remember any changes done to World Wall.")
    except Exception as e:
        print("\nUnfortunately, I won't remember changes done to the World Wall, but thanks for using it.")
        print(e)


def add_new_pair():
    print("\nYou wanna add a new pair? Nice! Here is what I need.")
    new_word = input("Please give the WORD: ")
    new_description = input("Please give its DESCRIPTION: ")

    new_meaning = {'description': new_description, 'category': None} # to minimize duplication

    if (new_word, new_meaning) in world_wall.items():
        # Your program must not allow duplicate entries.
        print("\nWe've got this in the dictionary already!")
    else:
        # Your program should give users the option to modify an existing meaning.
        world_wall[new_word] = new_meaning
        print(f"\nYour new pair '{new_word}'- '{new_description}' was added to the dict.")


def categorize_word():
    word = input("Enter word you would like to categorize: ")
    category = input("Give category for that word: ")
    world_wall[word] = {'description': get_description(word), 'category': category}


def get_description(word):
    meaning = world_wall[word] # mini dict extracted from big dict
    return meaning['description'] # desc. extracted from mini dict


def modify_word():
    old_word = input("Please enter word you would like to modify its spelling: ")
    new_word = input("Please enter word with correct spelling: ")
    world_wall[new_word] = world_wall[old_word]
    del world_wall[old_word]
    print(f"'{old_word}' was re-spelled into '{new_word}'")


def play_game():
    print("Great, this will be fun!")
    random_word = random.choice(list(world_wall.keys()))
    corresponding_description = get_description(random_word)
    print(f"Guess the word: '{corresponding_description}'")
    guessed_word = ""
    while guessed_word != random_word:
        guessed_word = input("Your suggestion: ")
        if guessed_word == random_word:
            print("Nice! You've guessed it right!")
        else:
            print("Guess again!")



#### MAIN PROGRAM ####
display_title()

datafile: str = "world_wall_bonus" # filename, to eliminate duplication in load and exit

world_wall = load_world_wall()
choice = ""

while choice != "q":
    # get user's choice (as string)
    choice = get_choice()

    if choice == "1":
        see_dict()
    elif choice == "2":
        add_new_pair()
    elif choice == "3":
        categorize_word()
    elif choice == "4":
        modify_word()
    elif choice == "5":
        play_game()
    elif choice == "q":
        quit()
    else:
        print("\nPlease, re-enter your choice.")

# (later on) Turn your program into a website that only you can use.
# (later on) Turn your program into a website that anyone can register for, and use.
# Add a visualization feature that reports on some statistics about the words and meanings that have been entered.