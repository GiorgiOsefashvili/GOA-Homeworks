def valid_braces(string):

    brace_map = {')': '(', ']': '[', '}': '{'}

    stack = []


    for char in string:

        if char in brace_map.values():
            stack.append(char)

        elif char in brace_map.keys():

            if stack == [] or brace_map[char] != stack.pop():
                return False


    return stack == []

print(valid_braces("(){}[]"))  
print(valid_braces("(}"))      

