# Define the registered password
registered_password = "password123"

# Use a while loop to repeatedly ask for the password until it matches
while True:
    # Ask the user to input the password
    user_password = input("Please enter the password: ")

    # Check if the user's password matches the registered password
    if user_password == registered_password:
        print("Access granted!")
        break  # Exit the loop since the password is correct
    else:
        print("Incorrect password. Please try again.")
