def longest_palindrome(s):
    longest = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                longest = max(longest, len(substring))
    return longest

print(longest_palindrome("baba"))