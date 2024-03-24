def longest_happy_prefix(s):
    n = len(s)
    for i in range(n - 1, 0, -1):
        if s[:i] == s[-i:]:
            return s[:i]
        
    return ""

if __name__=="__main__":
    input_string = input()
    print(longest_happy_prefix(input_string))