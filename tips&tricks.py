dogs = ['border collie', 'whippet', 'australian cattle dog', 'labrador retriever']

# assesing one item in the list
dog = dogs[2]

# insert where and what
dogs.insert(1, 'basenji')

#appending
dogs.append('pit bull')

# is it in the list (T/F)
print('saluki' in dogs)

# sorting the list
original_dogs = dogs
dogs.sort()     # nema return
dogs.sort(reverse=True) #  nema return
print(sorted(original_dogs))
print(original_dogs)

# length
number_of_dogs = len(dogs)

# find its location
print(dogs.index('whippet'))

# Use the in function to show that this is in your list.
print('basenji' in dogs)

# remove item from a list
del dogs[0]
dogs.remove('basenji') # only the first item with this value is removed

# popping item from a list
popped_out = dogs.pop() # popps out the last one
popped_out = dogs.pop(0) # popps out the first one

print(popped_out)

#slicing
new_list = dogs[:3] # includes dogs at positions 0, 1 and 2
new_list_two = dogs[2:5] # includes dogs at positions 2, 3 and 4

# copy a list
copied_dogs = dogs[:] # all

# using range
for number in range(1,21,2):    # (from, to, step)
    print(number)

# Create a list of the first ten numbers.
numbers = list(range(1,11))
print(numbers)

# The min(), max(), and sum() functions
ages = [23, 16, 14, 28, 19, 11, 38]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

# numerical comprehension
squares = [number**2 for number in range(1,11)]

# non-numerical comprehension
students = ['bernice', 'aaron', 'cody']
great_students = [student.title() + " the great!" for student in students]

# slicing strings
message = "Hello World!"
first_char = message[0]

#Finding substrings
message = "I like cats and dogs."
dog_present = 'dog' in message
print(dog_present)

#Replacing substrings
message = "I like cats and dogs, but I'd much rather own a dog."
message = message.replace('dog', 'snake')

# Count substrings
message = "I like cats and dogs, but I'd much rather own a dog."
number_dogs = message.count('dog')

#Splitting strings
message = "I like cats and dogs, but I'd much rather own a dog."
words = message.split(' ') # splitted by SPACE

