def sum_unique(lst):
    from collections import Counter
    
    # Count occurrences of each element in the list
    counts = Counter(lst)
    
    # Sum elements that appear exactly once
    result = sum(item for item in lst if counts[item] == 1)
    
    return result

# Test cases
print(sum_unique([3, 4, 3, 6]))            # 10
print(sum_unique([1, 10, 3, 10, 10]))      # 4
print(sum_unique([1, 2, 2, 3, 4, 4, 5]))   # 9
print(sum_unique([5, 5, 5, 5, 5, 5, 5]))   # 0
print(sum_unique([7, 8, 9, 7, 10, 9, 11])) # 18


