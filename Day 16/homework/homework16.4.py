def find_largest_number(numbers):
    if not numbers:
        return None  
    largest_number = numbers[0]
    for num in numbers[1:]:
        if num > largest_number:
            largest_number = num
    return largest_number

input_numbers = [1, 4, 21, 13, 7]
largest_number = find_largest_number(input_numbers)
print("The largest number in the list is:", largest_number)
