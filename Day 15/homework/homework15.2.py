def main():
    correct_password = "Goa best"
    incorrect_attempts = 0

    while True:
        password = input("Enter the password: ")
        if password == correct_password:
            print("Congratulations! You entered the correct password.")
            break
        else:
            incorrect_attempts += 1
            print("Incorrect password. Please try again.")
    
    print(f"Number of incorrect attempts: {incorrect_attempts}")

if __name__ == "__main__":
    main()
