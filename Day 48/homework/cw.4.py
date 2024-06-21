def check_exam(arr1, arr2):
    score = 0
    for correct, student in zip(arr1, arr2):
        if student == '':
            score += 0
        elif student == correct:
            score += 4
        else:
            score -= 1
    return max(score, 0)

print(check_exam(["a", "b", "c", "d"], ["a", "b", "c", "d"]))  
print(check_exam(["a", "b", "c", "d"], ["a", "b", "x", "d"]))  
print(check_exam(["a", "b", "c", "d"], ["a", "b", "", "d"]))  
print(check_exam(["a", "b", "c", "d"], ["a", "x", "x", "d"]))  
