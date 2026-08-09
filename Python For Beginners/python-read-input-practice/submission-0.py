def add_two_numbers() -> int:
    user_input = input()
    numbers = user_input.split(",")
    total_sum = 0
    for num in numbers:
        total_sum += int(num)
    return total_sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
