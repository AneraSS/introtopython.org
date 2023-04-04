# Tuples are basically lists that can never be changed.
# Technically, lists are mutable objects and tuples are immutable objects.
# Mutable objects can change (think of mutations), and immutable objects can not change.

# http://introtopython.org/lists_tuples.html

animals = ['dog', 'cat', 'bear']
animal = animals[0]

print("I have a %s" %animal)
print("I have a %s, a %s, and a %s." %(animals[0], animals[1], animals[2]))

number = 23
print("My favorite number is " + str(number) + ".")
print("My favorite number is %d." % number)

names = ['eric', 'ever']
numbers = [23, 2]
print("%s's favourite number is %d, while %s's is number %d." %(names[0].title(), numbers[1], names[1].title(), numbers[0]))

# Gymnast Scores
scores = tuple(range(1,11))
print("The lowest possible score is %d, and the highest possible score is %d." %(min(scores), max(scores)))
print(f"The lowest possible score is {min(scores)}, and the highest possible score is {max(scores)}.")