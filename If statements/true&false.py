# Write a program that consists of at least ten lines, each of which has a logical statement on it.
# The output of your program should be 5 Trues and 5 Falses.


numbers = [3,5,6,78,999,321,234,5667,23,6,8890,23,99,32,321,4566,78,42,1,2345,678,865,321,2345,78,2345,24556]

for number in numbers:
    if number > 345:
        print(f"{number} is larger than 345")
    if number < 45:
        print(f"{number} is lower than 45")

for number in numbers:
    if number > 25:
        print("True")
    else:
        print("False")