python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

# Show the words that are currently in the dictionary.
print("The following Python words have been defined:")
for word in python_words:
    print("- %s" % word)

requested_word = ''
while requested_word != 'quit':
    # Allow the user to choose a word, and then display the meaning for that word.
    requested_word = input("\nWhat word would you like to learn about? (or 'quit') ")
    if requested_word in python_words.keys():
        print("\n  %s: %s" % (requested_word, python_words[requested_word]))
    else:
        # Handle misspellings, and words not yet stored.
        print("\n  Sorry, I don't know that word.")