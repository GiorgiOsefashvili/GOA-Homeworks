def remove_duplicates(numbers):
    return list(set(numbers))

numbers_list = [1, 2, 3, 4, 5, 1, 2, 3, 4,8,9,9,9]

filtered_numbers = remove_duplicates(numbers_list)
print("Filtered list without duplicates:", filtered_numbers)
