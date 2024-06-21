def manual_sum(list):
    total = 0
    for num in list:
        total += num
    return total

numbers = [11,24,58]
print("Sum of numbers:", manual_sum(numbers))
