def square_numbers(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

input_numbers = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_numbers)
print("List of squares:", squared_list)
