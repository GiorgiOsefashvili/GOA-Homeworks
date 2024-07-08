def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
        
print(find_it([77,3,3,4,5,2,5,2,3,24]))