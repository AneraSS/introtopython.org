message = "Hi, Python!"
print (message)

# Store a message in a variable, and then print that message.
# Store a new message in the same variable, and then print that new message.

first_example = "Hello world."
print(first_example)

first_example = "New message with same variable name"
print(first_example)

# combining strings

first_name = 'ada'
second_name = 'lovelace'

full_name = first_name.title() + ' ' + second_name.title()
print (full_name)

full_name_two = first_name + ' ' + second_name
message = full_name_two.title() + " was considered the world's first computer programmer."
print(message)

print("Hello \teveryone!")
print("Hello \neveryone!")
print("Hello \n\teveryone!")

name = ' eric '
print(name.lstrip())
print(name.rstrip())
print(name.strip())

quote = "When you stop expecting people to be perfect, you can like them for who they are."
introduction = f"'{quote}' was said by Donald Miller, A Million Miles in a " \
               f"Thousand Years: What I Learned While Editing My Life."
print (introduction)

my_name = 'anera'
my_surname = 'svarc'
my_full_name = my_name + ' ' + my_surname
print(my_full_name.lower())
print(my_full_name.title())
print(my_full_name.upper())