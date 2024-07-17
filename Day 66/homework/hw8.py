def most_common(s):
    # Step 1: Count frequencies of each character
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    
    sorted_chars = sorted(frequency.items(), key=lambda item: (-item[1], s.index(item[0])))
  
    result = []
    for char, freq in sorted_chars:
        result.append(char * freq)
    
    return ''.join(result)


print(most_common("lfggglglsf"))  

