import os


def display_title():
    os.system('cls')
    print("************************************************************************************************************")
    print("***************************** W O R L D   W A L L **********************************************************")
    print("* A word wall is a place on your wall where you keep track of the new words and meanings you are learning. *")
    print("************************************************************************************************************")


def create_dict():
    key = input("Please, enter the WORD: ")
    value = input("Please, enter the MEANING of the word: ")
    return {key: value}


def see_dict():
    print("\nHere are all words and meanings entered thus far:")
    for name, meaning in world_wall.items():
        print(f"- {name.title()} means {meaning}.")


def get_choice():
    print("\nEnter [1] to see all words and meanings entered thus far.")
    print("Enter [2] to enter new word-meaning pair.")
    print("Enter [q] to quit.")
    return input()


display_title()

world_wall = {"riu":"dog"}
choice = ""

while choice != "q":
    choice = get_choice() # choice je string

    if choice == "1":
        see_dict()
