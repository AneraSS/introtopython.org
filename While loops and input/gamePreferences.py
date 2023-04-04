def print_game(games):
    for game in games:
        print(f"- {game.title()}")


games = ['horizon', 'last of us', 'tetris', 'rocket league', 'factorio']

print("I like these games: ")
print_game(games)

new_game = input("What game do you like? ")
games.append(new_game)

print(f"{new_game.title()} was added to the list: ")
print_game(games)

# make print_game a pure function (results with RETURN)