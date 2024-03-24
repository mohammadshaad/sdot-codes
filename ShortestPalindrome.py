def shortest_palindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    
    for i in range(len(s), -1, -1):
        if s[:i] == s[:i][::-1]:
            return s[i:][::-1] + s

input_str = input().strip()
print(shortest_palindrome(input_str))
