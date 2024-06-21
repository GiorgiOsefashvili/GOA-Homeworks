def manual_min(sia):
    min_value = sia[0]  
    for num in sia:
        if num < min_value:
            min_value = num
    return min_value

numbers = [3, 7, 2, 9, 5,-5]
print("Minimum value:", manual_min(numbers))
