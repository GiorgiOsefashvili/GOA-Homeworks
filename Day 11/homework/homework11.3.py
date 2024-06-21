# Initialize the sum variable
total_sum = 0

# Prompt the user for numbers until they enter 0
print("Enter numbers to sum. Enter 0 to finish.")

while True:
    # Take input from the user
    num = float(input("Enter a number: "))
    
    # Check if the user entered 0 to finish
    if num == 0:
        break  # Exit the loop if 0 is entered
    
    # Add the number to the total sum
    total_sum += num

# Print the total sum
print("The sum of the numbers is:", total_sum)
