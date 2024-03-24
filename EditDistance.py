def min_operations(s1, s2):
    # Initialize a 2D array to store the minimum number of operations
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize the first row and column with incremental values
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for j in range(len(s2) + 1):
        dp[0][j] = j

    # Fill the dp array
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If the characters at the current positions are the same
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Otherwise, choose the minimum of three possible operations
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    # The bottom-right cell contains the minimum number of operations
    return dp[len(s1)][len(s2)]

# Input parsing
s1 = input().strip()
s2 = input().strip()

# Call the min_operations function and print the result
print(min_operations(s1, s2))
