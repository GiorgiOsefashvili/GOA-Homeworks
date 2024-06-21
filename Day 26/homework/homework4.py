def manual_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

my_list = [1, 2, 3, 4, 5]
print("Length of the list:", manual_len(my_list))
