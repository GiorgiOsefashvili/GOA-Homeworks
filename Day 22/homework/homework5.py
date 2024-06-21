# DESCRIPTION:
# Write an algorithm that takes an array and moves all of the
# zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

#ამოხსნა

def move_zeros(array):
    zero_count = 0
    
    for i in range(len(array)):
        if array[i] != 0:
            array[zero_count] = array[i]
            zero_count += 1
    
    for i in range(zero_count, len(array)):
        array[i] = 0
    
    return array

print(move_zeros([4,0,15,8,0,5,7,0,9]))