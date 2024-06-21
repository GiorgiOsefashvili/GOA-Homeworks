def manual_reduce(number_list):
    copied_list = [] 
    for i in number_list:
        copied_list.append(i) 
    return copied_list

number_list= [5,7,3,4,1]
copied_list = manual_reduce(number_list)

print("Original list:", number_list)
print("Copied list:", copied_list)
