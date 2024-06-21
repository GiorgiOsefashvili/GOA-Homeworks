def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = filter_even_numbers(input_numbers)
print("Even numbers from the original list:", even_numbers_list)
