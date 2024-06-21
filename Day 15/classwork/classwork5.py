user_num =int(input("enter number"))
second_num = user_num + 10

new_list=[]
for i in range(user_num,second_num):
    new_list.append(i)
    print(new_list[::2])
