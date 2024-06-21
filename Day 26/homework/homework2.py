def manual_max(list):
    max_value = list[0] 
    for num in list:
        if num > max_value:
            max_value = num
    return max_value

numbers = [3, 7, 2, 9, 5]
print("Maximum value:", manual_max(numbers))
