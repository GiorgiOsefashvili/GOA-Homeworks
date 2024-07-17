def merge_strings(first, second):
    max_overlap = 0
    
    
    for i in range(1, min(len(first), len(second)) + 1):
        if first[-i:] == second[:i]:
            max_overlap = i
    

    return first + second[max_overlap:]


print(merge_strings("gio", "rgi"))  
print(merge_strings("luk", "uka"))  
print(merge_strings("abc", "def"))  
print(merge_strings("abc", "abc"))

