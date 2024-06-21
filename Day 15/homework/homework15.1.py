def next_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is not even.")
        print(f"The next even number is {number + 1}.")

def main():
    try:
        number = int(input("Please enter a number: "))
        next_even(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
