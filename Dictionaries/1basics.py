# dictionary_name = {key_1: value_1, key_2: value_2, key_3: value_3}
#
# dictionary_name = {key_1: value_1,
#                    key_2: value_2,
#                    key_3: value_3,
#                    }

python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

# Print out the items in the dictionary.
for word, meaning in python_words.items():
    print("\nWord: %s" % word)
    print("Meaning: %s" % meaning)


# for key_name, value_name in dictionary_name.items():
#     print(key_name) => The key is stored in whatever you called the first variable.
#     print(value_name) => The value associated with that key is stored in your second variable.