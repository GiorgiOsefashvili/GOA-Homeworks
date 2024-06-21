# DESCRIPTION:
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


#ამოხსნა


def solution(s):
    result = ""
    for char in s:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result


print(solution("giorGiosefashvili"))