students = ['bernice', 'aaron', 'cody']

for student in students:
    print(f"Hi, {student.title()}!")

dogs = ['border collie', 'whippet', 'australian cattle dog', 'labrador retriever']
# assesing one item in the list
print(dogs[1])
dog = dogs[2]
print(dog.title())
dog = dogs[-1]
print(dog.title())

languages = ['python', 'java', 'c']
print(languages[0])
print(languages[1])
print(languages[2])

for language in languages:
    print(f"A nice programming language is {language}.")

print(f"One item from my list is {languages[-1]}")

print("\n")
# The enumerate() function tracks the index of each item for you, as it loops through the list:
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Results for the dog show are as follows:")
for index, dog in enumerate(dogs):
    place = str(index + 1)
    print("\tPlace: " + place + " Dog: " + dog.title())


# Repeat First List, but this time use a loop to print out each value in the list.
riu_traits = ['whippet', 'cutie-pie', 'big nose', 'dangerous dog']
print("Riu is")
for riu_trait in riu_traits:
    print(f"\tsuch a {riu_trait}")

print("\nModifying elements in a list")
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs[0] = 'australian shepherd'
print(dogs)

print ("Finding an element in a list")
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print(dogs.index('australian cattle dog'))
print('australian cattle dog' in dogs)
print('poodle' in dogs)
dogs.append('poodle')
dogs.insert(1, 'whippet')


print("Users, hello!")
usernames = []
usernames.append('anna')
usernames.append('ruth')
usernames.append('martin')
usernames.append('tom')

for username in usernames:
    print(f"Welcome, {username.title()}!")

print(f"Thank you for being our first user, {usernames[0]}!")
print(f"Thank you for being our latest user, {usernames[-1]}!")

students = usernames

list_of_students = []
for student in sorted(students, reverse=True):
    list_of_students.append(student.title())
print(list_of_students)

numbers = [1, 3, 4, 2]
numbers.sort()
print(numbers)
# sorted() preserves the original order of the list:

user_count = len(students)
print(f"There are")

# working list
careers = ['chef', 'chemist', 'programmer', 'truck driver']
print(careers.index('chemist'))
print('chef' in careers)
careers.append('pianist')
print(careers)
careers.insert(0, 'doctor')
print(careers)
for career in careers:
    print(career)

# Starting From Empty
cats = []
cats.append('stray')
cats.append('persian')
cats.append('ocelot')
cats.append('tiger')
cats.append('lion')
print(cats)
print(f"The first cat in the list is the {cats[0]} cat.")
print(f"The last cat in the list is the {cats[-1]}.")

#Ordered Working List
print(f"Original list order: {careers}")
print(f"List in alphabetical order: {sorted(careers)}")
print(f"Original list order: {careers}")
print(f"Decreasing list order: {sorted(careers, reverse=True)}")
print(f"Original list order: {careers}")
print(f"Permanently sorted list in alphabetical order: {careers.sort()}.") # nema return!
careers.sort()
print(f"Permanently sorted list in alphabetical order: {careers}.")
print(f"Permanently sorted list in reverse alphabetical order: {careers.sort(reverse=True)}.") # nema return
careers.sort(reverse=True)
print(f"Permanently sorted list in reverse alphabetical order: {careers}.")

#Ordered Numbers
numbers = [2, 45, 67, 432, 57, 21, 567]
# using for loop
print("Original order:")
for number in numbers:
    print(number)
print("Increasing order:")
for number in sorted(numbers):
    print(number)
print("Decreasing order:")
for number in sorted(numbers, reverse=True):
    print(number)
print("Original order:")
for number in numbers:
    print(number)
print("Reverse order of how they started:")
numbers.reverse()
for number in numbers:
    print(number)
print("Original order")
for number in numbers:
    print(number)
print("Permanently, increasing.")
numbers.sort()
for number in numbers:
    print(number)
print("Permanently, decreasing.")
numbers.sort(reverse=True)
for number in numbers:
    print(number)

print(f"There are listed {len(careers)} careers.")
print(f"There are {len(numbers)} numbers in the list.")

# Famous people
famous_people = ['britney', 'madonna', 'j.lo', 'MJ']
pop_out = famous_people.pop()
pop_out = famous_people.pop(1)
famous_people.remove('j.lo')
del famous_people[0]

print(famous_people)

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab a batch from the middle of the list.
middle_batch = usernames[1:4]

for user in middle_batch:
    print(user.title())

# Alphabet Slices
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f"First three letters of the alphabet: {alphabet[:3]}")
middle = len(alphabet)/2
start = middle - 1
end = middle + 1
print(f"Three letters from the middle of the alphabet: {alphabet[3:6]}")
print(start)
print(f"Three letters from the end of the alphabet: {alphabet[5:]}")

# Protected List
people = ['ruth', 'tom', 'martin', 'mary']
new_people = people[:]
new_people.append('vesna')
new_people.append('gloria')

for person in people:
    print(f"{person.title()} is from the original list.")

for person in new_people:
    print(f"{person.title()} is from the new list.")

# Excercising with numbers
numbers = list(range(1,21))

wallets = [45, 67, 8764, 21, 345, 6889, 321]
print(f"The fattest wallet has ${max(wallets)} value in it.")
print(f"The skinniest wallet has ${min(wallets)} value in it.")
print(f"All together, these wallets have ${sum(wallets)} value in them.")

# Store the first ten square numbers in a list.
# Make an empty list that will hold our square numbers.
squares = []

# Go through the first ten numbers, square them, and add them to our list.
for number in range(1,11):
    squares.append(number**2)
print(squares)

# or written more comprehensive:
squares = [number**2 for number in range(1,11)]

# Multiples of Ten
multiples = [number*10 for number in range(10,101,10)]
print(multiples)

# cubes
cube = [number**3 for number in range(1, 11)]
print(cube)

# Awesomeness
names = ['ruth', 'martin', 'tom', 'vesna', 'gloria']
awesomeness = [name.title() + " you're awesome!" for name in names]
print(awesomeness)

# Working Backwards
#plus_thirteen = [number + 13 for number in range(1,11)]
plus_thirteen = []

for number in range (1,11):
    plus_thirteen.append(number+13)
print(plus_thirteen)

#Strings as a list of characters
message = "Hello world!"
message_list = list(message)
print(message_list)

# Slicing strings
message = "Hello World!"
first_three = message[:3]
last_three = message[-3:]
print(first_three, last_three)

#If you want to know where a substring appears in a string, you can use the find() method.
# The find() method tells you the index at which the substring begins.
message = "I like cats and dogs."
dog_index = message.find('dog')
print(dog_index)

message = "I like cats and dogs, but I'd much rather own a dog."
words = message.split(' ')
print(words)

# Listing a Sentence
sentence = "Use a for loop to print each character from your sentence on a separate line."
for letter in sentence:
    print(letter)

#Sentence List
# Store a single sentence in a variable. Create a list from your sentence.
# Print your raw list (don't use a loop, just print the list).

sentence = "Create a list from your sentence."
print(list(sentence))

print(sentence.split(" "))

# Sentence Slices
sentence = "Using slices, print out the first five characters, any five consecutive characters from the middle of " \
           "the sentence, and the last five characters of the sentence."

middle = int(len(sentence)/2)
print(middle)
start = middle - 2
end = middle + 3
print(f"First five characters are: *{sentence[:5]}*, middle five are: *{sentence[start:end]}*, "
      f"last five are: *{sentence[-6:]}*")

# Finding Python
sentence = "Store a sentence containing Python in a variable, " \
           "making sure you use the word Python at least twice in the sentence."

#Use the in keyword to prove that the word Python is actually in the sentence.
print('Python' in sentence)
# Use the find() function to show where the word Python first appears in the sentence.
print(sentence.find('Python'))
# Use the rfind() function to show the last place Python appears in the sentence.
print(sentence.rfind('Python'))
# Use the count() function to show how many times the word Python appears in your sentence.
print(sentence.count('Python'))
# Use the split() function to break your sentence into a list of words.
print(sentence.split(' '))
# Print the raw list, and use a loop to print each word on its own line.
sentence_list = sentence.split(' ')
for word in sentence_list:
    print (word)
# Use the replace() function to change Python to Ruby in your sentence.
print(sentence.replace('Python', 'Ruby'))

# https://rosalind.info/problems/dna/
# Counting DNA Nucleotides
DNA_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_A = 0
count_G = 0
count_C = 0
count_T = 0

for letter in DNA_string:
    if letter == "A":
        count_A += 1
    if letter == "G":
        count_G += 1
    if letter == "C":
        count_C += 1
    if letter == "T":
        count_T += 1

print (f"{count_A} {count_C} {count_G} {count_T}")

# https://rosalind.info/problems/rna/
# Transcribing DNA into RNA
DNA_string = "GATGGAACTTGACTACGTAAATT"
RNA_string = DNA_string.replace("T", "U")

result = "GAUGGAACUUGACUACGUAAAUU"
if RNA_string == result:
    print("You wrote the correct code.")
else:
    print("Re-write your code.")

# https://rosalind.info/problems/revc/
# Complementing a Strand of DNA
DNA_string = "AAAACCCGGT"
DNA_complementary_string = ""

for letter in DNA_string:
    if letter == "A":
        complementary_letter = "T"
        DNA_complementary_string += complementary_letter
    if letter == "T":
        complementary_letter = "A"
        DNA_complementary_string += complementary_letter
    if letter == "G":
        complementary_letter = "C"
        DNA_complementary_string += complementary_letter
    if letter == "C":
        complementary_letter = "G"
        DNA_complementary_string += complementary_letter

print(DNA_string)
print(DNA_complementary_string)

DNA_complementary_string_reversed = ""

for letter in DNA_complementary_string[::-1]:
    DNA_complementary_string_reversed += letter

print(DNA_complementary_string_reversed)

#txt = "Hello World"[::-1]
#print(txt)

result2 = "ACCGGGTTTT"
if DNA_complementary_string_reversed == result2:
    print ("You got it right!")
else:
    print("Re-write!")