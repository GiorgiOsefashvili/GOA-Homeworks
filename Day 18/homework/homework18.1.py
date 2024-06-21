def filter_fours(numbers):
    filtered_list = [num for num in numbers if num % 4 == 0]
    return filtered_list

all_numbers = list(range(1, 21))

filtered_numbers = filter_fours(all_numbers)

print("ყველა 4-ის ჯერადი რიცხვი 1-დან 20-მდე:", filtered_numbers)
