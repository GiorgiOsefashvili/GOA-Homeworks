# Define the correct PIN
correct_pin = "1234"

# Initialize the balance
balance = 1000

# Ask the user to enter their PIN
pin_attempt = input("Enter your PIN: ")

# Check if the entered PIN is correct
if pin_attempt == correct_pin:
    print("PIN accepted.")
    while True:
        # Display options to the user
        print("\nChoose an option:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

        # Take user's choice
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform actions based on the user's choice
        if choice == "1":
            withdrawal_amount = float(input("Enter the amount to withdraw: "))
            if withdrawal_amount <= balance:
                balance -= withdrawal_amount
                print("Withdrawal successful. Your new balance is:", balance)
            else:
                print("Insufficient funds.")
        elif choice == "2":
            deposit_amount = float(input("Enter the amount to deposit: "))
            balance += deposit_amount
            print("Deposit successful. Your new balance is:", balance)
        elif choice == "3":
            print("Your balance is:", balance)
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")
else:
    print("Incorrect PIN. Please try again later.")
