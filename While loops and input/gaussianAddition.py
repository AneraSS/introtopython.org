def pop_out(numbers):
    value1 = numbers.pop(0)
    value2 = numbers.pop(-1)
    result = value1 + value2
    return (value1, value2, result)

def calc_sum(numbers):
    count = 0
    sum_of_numbers = 0
    while len(numbers) != 0:
        count += 1
        value1, value2, result = pop_out(numbers)
        sum_of_numbers += result
        print(f"#{count}: {value1} + {value2} = {result}")
    print(f"Total count: {count}")
    return sum_of_numbers


numbers = list(range(1, 101))

print(f"Gauss' multiplication: {calc_sum(numbers)}")

