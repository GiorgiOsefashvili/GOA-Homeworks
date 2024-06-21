#DESCRIPTION
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

#ამოხსნა


def high_and_low(numbers):
    numbers_list = list(map(int, numbers.split()))
    maximum = max(numbers_list)
    minimum = min(numbers_list)

    return f"{maximum} {minimum}"

print(high_and_low("12 51 154 -240 4"))