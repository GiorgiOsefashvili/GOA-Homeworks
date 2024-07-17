def factorial_division(n, d):
    sum = 1
    for i in range(d+1,n+1):
        sum *= i
    return sum

print(factorial_division(5,1))