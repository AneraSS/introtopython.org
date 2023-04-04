# This program stores people's favorite numbers, and displays them.
favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
for name in favorite_numbers:
    print("\n%s's favorite numbers are:" % name.title())

    # Each value is itself a list, so let's put that list in a variable.
    current_favorite_numbers = favorite_numbers[name]
    for favorite_number in current_favorite_numbers:
        print(favorite_number)