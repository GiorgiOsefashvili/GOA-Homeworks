def manual_reverse(collection):
    reversed_collection = []
    
    for i in range(len(collection) - 1, -1, -1):
        reversed_collection.append(collection[i])
    
    return reversed_collection

sorted_list = [1, 2, 3, 4, 5]
reversed_list = manual_reverse(sorted_list)
print(reversed_list)  
