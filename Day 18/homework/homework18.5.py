def average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    length = len(numbers)
    return total / length

numbers_list = [5, 10, 15, 20, 25]

avg = average(numbers_list)
print("სიის საშუალო არითმეტიკული:", avg)
