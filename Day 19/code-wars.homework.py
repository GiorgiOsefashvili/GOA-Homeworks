# DESCRIPTION:
# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.


# My solution

# def findSmallestInt(arr):
#     min = arr[0]
#     for item in arr:
#         if min > item:
#             min = item
#     return min

# "პირველი დავალება"


# DESCRIPTION:
# Write a function that removes the spaces from the string, then return the resultant string.

# Examples:

# Input -> Output
# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"


# Solution

# def no_space(x):
#     str_char = ''
#     for i in range(len(x)):
#         if x[i] == ' ':
#             continue
#         else:
#             str_char = str_char + x[i]
#     return str_char

# "მეორე დავალება "

# DESCRIPTION:
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

# solution 

# def boolean_to_string(b):
#     return str(b)

# "მესამე დავალება "

# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.


# solution

def sum_array(a):
    total = 0
    i = 0
    while i < len(a):
        total += a[i]
        i += 1
    return total
