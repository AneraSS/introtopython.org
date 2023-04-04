def get_number_word(number):
    # Takes in a numerical value, and returns
    #  the word corresponding to that number.
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    else:
        return "I'm sorry, I don't know that number."


# Let's try out our function.
for current_number in range(0, 6):
    number_word = get_number_word(current_number)
    print(current_number, number_word)