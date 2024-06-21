def add_name_to_list(first_name, last_name, name_list):
    full_name = f"{first_name} {last_name}"
    name_list.append(full_name)
    return name_list

names_list = ["Luka javaxishvili", "budu zivzivadze"]
first_name = input("enter your name: ")
last_name = input("enter your surname: ")

updated_list = add_name_to_list(first_name, last_name, names_list)
print("updated list:", updated_list)
