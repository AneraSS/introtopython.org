new_game = ""
games = []

while new_game != "q":
    new_game = input("Please, add a game (q for quit): ")
    if new_game != "q":
        games.append(new_game)

print(games)