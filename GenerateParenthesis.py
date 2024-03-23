def generateParenthesis(n):
    def generateParenthesisHelper(openCount, closeCount, current, result):
        if len(current) == 2 * n:
            result.append(current)
            return
        if openCount < n:
            generateParenthesisHelper(openCount + 1, closeCount, current + "(", result)
        if closeCount < openCount:
            generateParenthesisHelper(openCount, closeCount + 1, current + ")", result)
            
    result = []  # Initialize result list here
    generateParenthesisHelper(0, 0, "", result)
    return result

if __name__ == "__main__":
    n = int(input())
    combinations = generateParenthesis(n)
     
    for combination in combinations:
        print(combination)