import os
import pickle

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
        print(f"- {name.title()} means {meaning}.")


def get_choice():
    print("\nEnter [1] to see all words and meanings entered thus far.")
    print("Enter [2] to enter new word-meaning pair.")
    print("Enter [q] to quit.")
    return input()


def load_world_wall():
    # loads from file and puts them in dict "world_wall
    # if doesn't exist, creates an empty one
    try:
        file_object = open("world_wall", "rb")
        world_wall = pickle.load(file_object)
        file_object.close()
        return world_wall
    except Exception as e:
        print(e)
        return {}


def quit():
    # dumps into a file, and prints the quit message
    try:
        file_object = open("world_wall", "wb")
        pickle.dump(world_wall, file_object)
        file_object.close()
        print("\nThanks for using the World Wall. I'll remember any changes done to World Wall.")
    except Exception as e:
        print("\nUnfortunately, I won't remember changes done to the World Wall, but thanks for using it.")
        print(e)


def add_new_pair():
    print("\nYou wanna add a new pair? Nice! Here is what I need.")
    new_word = input("Please give the WORD: ")
    new_meaning = input("Please give its MEANING: ")

    if (new_word, new_meaning) in world_wall.items():
        print("\nWe've got this in the dictionary already!")
    else:
        world_wall[new_word] = new_meaning
        print(f"\nYour new pair '{new_word}'- '{new_meaning}' was added to the dict.")




#### MAIN PROGRAM ####
display_title()

world_wall = load_world_wall()
choice = ""

while choice != "q":
    # get user's choice (as string)
    choice = get_choice()

    if choice == "1":
        see_dict()
    elif choice == "2":
        add_new_pair()
    elif choice == "q":
        quit()
    else:
        print("\nPlease, re-enter your choice.")
