# When you run this program on your computer, look for the file animals.pydata in the same directory as the program
# file. If that worked, we need to modify the program so that the next time it runs it loads the data from
# animals.pydata back in. We do that with a try-except block at the beginning of the program,
# which tries to open the file and read the data back into the animals list. If that doesn't work, which will
# happen when the program is run for the first time or if you delete animals.pydata, we make the same empty
# list we had before.

import pickle

# This program asks the user for some animals, and stores them.
#  It loads animals if they exist.

# Try to load animals. If they don't exist, make an empty list
#  to store new animals in.
try:
    file_object = open('animals.pydata', 'rb') # (file_name, write in bytes)
    animals = pickle.load(file_object)
    file_object.close()
except:
    animals = []

# Show the animals that are stored so far.
if len(animals) > 0:
    print("I know the following animals: ")
    for animal in animals:
        print(animal)
else:
    print("I don't know any animals yet.")

# Create a loop that lets users store new animals.
new_animal = ''
while new_animal != 'quit':
    print("\nPlease tell me a new animal to remember.")
    new_animal = input("Enter 'quit' to quit: ")
    if new_animal != 'quit':
        animals.append(new_animal)

# Try to save the animals to the file 'animals.pydata'.
try:
    file_object = open('animals.pydata', 'wb')
    pickle.dump(animals, file_object)
    file_object.close()

    print("\nI will remember the following animals: ")
    for animal in animals:
        print(animal)
except Exception as e:
    print(e)
    print("\nI couldn't figure out how to store the animals. Sorry.")