def alphabet_position(text):

    text = text.lower()

    positions = []
    
    for char in text:

        if char.isalpha():

            position = ord(char) - ord('a') + 1

            positions.append(str(position))
    

    return ' '.join(positions)

 
print(alphabet_position("a"))  
print(alphabet_position("z")) 
print(alphabet_position("gio")) 