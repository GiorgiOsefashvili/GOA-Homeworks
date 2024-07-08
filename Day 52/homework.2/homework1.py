def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
            num_vowels += 1
    return num_vowels

Word = "Hello, World!"
print(getCount(Word))