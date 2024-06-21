# number_list = []

# for i in range(1,51):
#     number_list.append(i)

# print(number_list[0:50:3])

#/

# word = "Giorgi"
# print(word.replace("i" , "f"))

#///////!

# def my_replace(word,replace_char,input_char):
#     changed_word = ''

#     for char in word:
#         if char == replace_char:
#             changed_word = changed_word + input_char
#         else:
#             changed_word = changed_word +char
#     return changed_word

# print(my_replace("giorgi","g","f"))

#///////!

# print("giorgi".count ("g"))

# def my_count(collection,count_elements):
#     count = 0

#     for element in collection :
#         if element == count_elements:
#             count = count + 1

#     return count

# print(my_count("ablabuda","a"))

#///////!

# print("giorgi".find ("rgi"))

# def my_find(collection,value):
#     for index in range(len(collection)):
#         if collection[index] == value:
#             return index
#     return -1

# print(my_find([1,2,3,4,5], 2))


#////////!

# def replace_even_index(word,replace_char):
#     changed_word = ''
#     for index in range (len(word)):
#             changed_word = changed_word + replace_char
#     else:
#         changed_word = changed_word + word[index]

#     return changed_word
# print(replace_even_index("lukaa","k"))
    

#/////////!

# def find_last_even(number_list):
#     for i in range (len(number_list)-1,-1,-1):
#         if number_list [1] % 2 == 0:
#             return i

# print(find_last_even([1,2,3,4,5]))

# print("+".join(["1","2","3"]))


#//////!

def my_join(join_str,strings_list):
    joined_elements = ''

    for word in strings_list:
        joined_elements = join_str + word

    return joined_elements[1:]


print(my_join("+",[1,2,3]))
