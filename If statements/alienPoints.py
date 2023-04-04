aliens = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'orange', 'grey', 'black', 'white']

score = 0

for alien in aliens:
    if alien == "red":
        score += 5
    if alien == "green":
        score += 10
    if alien == "blue":
        score += 15

print(score)
