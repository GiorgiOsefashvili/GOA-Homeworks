def next_even(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is not even. Next even number is {num + 1}.")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        next_even(num)
    except ValueError:
        print("Please enter a valid integer.")
