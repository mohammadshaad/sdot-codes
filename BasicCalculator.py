def calculate(expression):
    stack = []
    num = 0
    sign = '+'
    
    for i in range(len(expression)):
        c = expression[i]
        
        if c.isdigit():
            num = num * 10 + int(c)
            
        if (not c.isdigit() and c != ' ') or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            sign = c
            num = 0
            
    return sum(stack)
expression = input()
result = calculate(expression)
print(result)