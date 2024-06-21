#DESCRIPTION
# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

#ამოხსნა

def find_short(s):
    words = s.split()
    find_short_name = [len(word) for word in words]

    return min(find_short_name)

s = "Georgia's located inss caucasus"

print(find_short(s))