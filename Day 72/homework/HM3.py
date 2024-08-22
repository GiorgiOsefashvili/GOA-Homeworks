def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        if num == sum(int(digit) ** (i + 1) for i, digit in enumerate(str(num))):
            result.append(num)
    return result

print(sum_dig_pow(1, 100))
print(sum_dig_pow(2, 7))
print(sum_dig_pow(10, 100))