num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1

sum_of_numbers = 0
for num in range(num1, num2 + 1):
    sum_of_numbers += num

print("Sum of numbers in the range:", sum_of_numbers)
