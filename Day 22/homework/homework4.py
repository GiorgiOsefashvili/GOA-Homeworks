# DESCRIPTION:
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


#ამოხსნა

def expanded_form(num):
    num_str = str(num)
    
    expanded_parts = []
    
    position = len(num_str) - 1
    
    for digit in num_str:
        if digit != '0':
            expanded_parts.append(digit + '0' * position)
        position -= 1
    
    return ' + '.join(expanded_parts)

print(expanded_form(5057))