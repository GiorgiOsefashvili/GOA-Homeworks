# Ask the user for a username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username and password are correct
if username == "admin" and password == "password123":
    print("Login successful")
else:
    print("Incorrect username or password")

