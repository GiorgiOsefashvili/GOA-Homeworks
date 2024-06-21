start_number = int(input("გთხოვთ, შეიყვანოთ რიცხვი: "))

new_list = []

for i in range(start_number, start_number + 11):
    new_list.append(i)

new_list.pop(2)  # მოვაშოროთ ელემენტი ინდექსით 2

print(new_list)
