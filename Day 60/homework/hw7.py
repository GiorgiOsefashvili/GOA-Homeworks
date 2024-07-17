def spot_diff(string1, string2):
    differences = []
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            differences.append(i)  
    
    return differences


string1 = "abcdefg"
string2 = "abcqetg"
result = spot_diff(string1, string2)
print(result)  
