def isMatch(pattern: str, input_str: str) -> bool:
    p_pointer = i_pointer = 0
    last_star_index = last_i_pointer = -1
    
    while i_pointer < len(input_str):
        if p_pointer < len(pattern) and (pattern[p_pointer] == '?' or pattern[p_pointer] == input_str[i_pointer]):
            p_pointer += 1
            i_pointer += 1
        elif p_pointer < len(pattern) and pattern[p_pointer] == '*':
            last_star_index = p_pointer
            last_i_pointer = i_pointer
            p_pointer += 1
        elif last_star_index != -1:
            p_pointer = last_star_index + 1
            last_i_pointer += 1
            i_pointer = last_i_pointer
        else:
            return False
    
    while p_pointer < len(pattern) and pattern[p_pointer] == '*':
        p_pointer += 1
    
    return p_pointer == len(pattern)


text = input().strip()
pattern = input().strip()

if isMatch(pattern, text):
    print("true")
else:
    print("false")