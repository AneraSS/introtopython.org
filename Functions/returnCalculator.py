# Modify Addition Calculator so that your function returns the sum of the two numbers.
# The printing should happen outside of the function.

def perform_addition(number1, number2):
    result = number1 + number2
    return result

print(f"Numbers {1} + {2} give {perform_addition(1,2)}")

num1 = 1
num2 = 3
print(f"Numbers {num1} + {num2} give {perform_addition(num1,num2)}")