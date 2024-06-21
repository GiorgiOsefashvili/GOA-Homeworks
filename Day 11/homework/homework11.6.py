# Ask the user for their age
age = int(input("Please enter your age: "))

# Determine the age range and print a message
if age < 0:
    print("Invalid age. Please enter a valid age.")
elif age < 13:
    print("You are a Child.")
elif age < 20:
    print("You are a Teenager.")
else:
    print("You are an Adult.")
