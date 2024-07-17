def round_to_next5(n):
    remainder = n % 5
    if remainder == 0:
        return n
    else:
        return n + (5 - remainder)

print(round_to_next5(7))
print(round_to_next5(2))   
print(round_to_next5(12))  

