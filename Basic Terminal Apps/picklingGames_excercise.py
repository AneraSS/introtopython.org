# Write a program that lets users enter a number of different games.
# Save the games to disk, using pickle, before the program closes.
# Load the games from the saved file at the beginning of your program.

import pickle

# Try to load games. If they don't exist, make an empty list
#  to store new games in.
try:
    file_object = open('games.pydata', 'rb') # read in bytes (binary?)
    games = pickle.load(file_object)
    file_object.close()
except:
    games = []

# Show games stored thus far.
for game in games:
    print(game)
else:
    print("No games saved yet.")

# Fill in the game list, by user.
new_game = ""

while new_game != 'q':
    print("To quit, enter 'q'.")
    new_game = input("Enter new game: ")

    if new_game in games:
        print("Already exists!")
    else:
        games.append(new_game)

    if new_game == 'q':
        games.remove("q")

# Try to save the games to the file 'games.pydata'.
try:
    file_object = open('games.pydata', 'wb')   # write in bytes
    pickle.dump(games, file_object)
    file_object.close()

    print("\nI will remember the following animals: ")
    for game in games:
        print(game)
except Exception as error:
    print(error)
    print("\nI couldn't figure out how to store the games. Sorry.")