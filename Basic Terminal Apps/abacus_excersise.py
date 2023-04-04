### FUNCTIONS ###
def display_title():
    print("********************************")
    print("********** A B A C U S *********")
    print("********************************")


def get_choice():
    print("\nTo quit, enter [q].")
    return input("Please, enter the year you want to depict as abacus number: ")


def quit():
    print("\n *** Thanks for using me as your Abacus! ***")


def depict_abacus(number):
    print(f"\nAbacus for number: {number}")

    for i in range(0, 4):
        line = int(number[i])

        # start and end point
        wall = "|"

        # left part
        left_integer = 9 - line
        left_depicted = "x" * left_integer

        # middle part
        middle_depicted = "-" * 6

        # right part
        right_depicted = "x" * line

        print(wall + left_depicted + middle_depicted + right_depicted + wall)


### MAIN CODE ###

display_title()

choice = ""

while choice != "q":
    choice = get_choice()

    if choice == "q":
        quit()
    elif int(choice) in range(1,9999):
        depict_abacus(choice)
    else:
        print("Please re-enter the 4-digit number.")