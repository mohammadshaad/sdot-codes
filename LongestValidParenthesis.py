def longest_valid_parentheses(s):
    stack=[-1]
    max_len=0
    for i,char in enumerate(s):
        if char=='(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len,i-stack[-1])
    return max_len
def convert_to_string(result):
    return str(result)
if __name__=="__main__":
    input_str=input()
    result=longest_valid_parentheses(input_str)
    print(convert_to_string(result))
