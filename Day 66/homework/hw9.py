import math

def is_equable_triangle(a, b, c):
    P = a + b + c
    
    s = P / 2

    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    if math.isclose(A, P):
        return True
    else:
        return False

print(is_equable_triangle(5, 12, 13))
print(is_equable_triangle(3, 4, 5))
