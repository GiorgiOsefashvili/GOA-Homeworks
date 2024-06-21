def transform_name(last_name):
    new_list = []
    for index, letter in enumerate(last_name):
        if index % 2 == 0:
            new_list.append(letter)
    return new_list

last_name = input("Enter your last name: ")

new_name = transform_name(last_name)
print("Transformed name:", new_name)
