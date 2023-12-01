import pickle


def load_PSE():
    try:
        file_object = open("PSE", "rb")
        PSE = pickle.load(file_object)
        file_object.close()
        return PSE
    except Exception as e:
        print(e)
        return {}

def load_PSE_short():
    try:
        file_object = open("PSE_short", "rb")
        PSE_short = pickle.load(file_object)
        file_object.close()
        return PSE_short
    except Exception as e:
        print(e)
        return {}

def quit():
    try:
        file_object = open("PSE", "wb")
        pickle.dump(PSE, file_object )
        file_object.close()
        print("Thanks for filling-up our dictionary with PSE information. Good-bye!")
    except Exception as e:
        print(e)
        print("Unfortunately, an error occurred and I cannot save the given infos. Sorry!")


def quit_short():
    try:
        file_object = open("PSE_short", "wb")
        pickle.dump(PSE_short, file_object )
        file_object.close()
    except Exception as e:
        print(e)


def get_choice():
    print("\nWhat would you like to do?")
    print("Pick -1- to enter a new element.")
    print("Pick -2- to see current elements.")
    print("Pick -3- to get info about an element.")
    print("Pick -q- to save and exit.")
    return input()

def add_element():
    name = input("Name: ")
    symbol = input("Symbol: ")
    atomic_number = input("Atomic number: ")
    row = input("Row: ")
    column = input("Column: ")
    PSE[name] = {"symbol": symbol, "atomic_number": atomic_number, "row": row, "column": column}
    PSE_short[symbol] = name

def show_elements():
    for key, value in PSE.items():
        print(f"- {key} ({value['symbol']}, Ar = {value['atomic_number']}, R: {value['row']}, C: {value['column']})")


def get_info():
    symbol = input("Provide the SYMBOL to get info about the element: ")
    print(PSE_short)
    name = PSE_short[symbol]
    print(display_element_information(name))


def display_element_information(name):
    print(f"So you wanna know about {name}")
    element_info = PSE[name]
    symbol = element_info['symbol']
    atomic_number = element_info['atomic_number']
    row = element_info['row']
    column = element_info['column']
    return ("symbol: " + symbol + ", Ar = " + atomic_number + ", R: " + row + ", C: " + column)


PSE = load_PSE()
PSE_short = load_PSE_short()
choice = ""

while choice != "q":
    choice = get_choice()

    if choice == "1":
        add_element()
    elif choice == "2":
        show_elements()
    elif choice == "3":
        get_info()
    elif choice == "q":
        quit()
        quit_short()
    else:
        print("Please, re-enter your choice.")