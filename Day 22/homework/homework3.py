# DESCRIPTION:
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)


#ამოხსნა

def find_outlier(integers):
    even_count = sum(1 for num in integers if num % 2 == 0)
    odd_count = len(integers) - even_count
    
    
    outlier = next((num for num in integers if (even_count > 1 and num % 2 != 0)
                    or (odd_count > 1 and num % 2 == 0)), None)
    
    return outlier

print(find_outlier([1,2,3,4,5]))
