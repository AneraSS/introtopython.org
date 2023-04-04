my_dict = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }


# looping through all key-value pairs:
for word, meaning in my_dict.items():

# looping through all keys:
for key in my_dict.keys():
# This is actually the default behavior of looping through the dictionary itself.
# So you can leave out the .keys() part, and get the exact same behavior.


# Allow the user to choose a word, and then display the meaning for that word.
requested_word = input("\nWhat word would you like to learn about? ")
print("\n%s: %s" % (requested_word, my_dict[requested_word]))

# Looping through all values in a dictionary
for value in my_dict.values():
    print('Value: %s' % value)

# sort keys
#  the words and meanings can be printed in alphabetical order
for word in sorted(my_dict.keys()):
    print(word)
    print("%s: %s" % (word.title(), my_dict[word]))







