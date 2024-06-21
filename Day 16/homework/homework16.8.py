def sum_greater_than_10(numbers):
    total = 0
    for num in numbers:
        if num > 10:
            total += num
    return total

input_numbers = [5, 12, 8, 15, 3, 20]
sum_of_numbers = sum_greater_than_10(input_numbers)
print("Sum of numbers greater than 10:", sum_of_numbers)
