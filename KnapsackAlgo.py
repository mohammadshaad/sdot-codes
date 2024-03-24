def knapsack(N, W, weights, values):
    # Initialize a 2D array to store the maximum value for each weight capacity
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # Iterate through each item
    for i in range(1, N + 1):
        # Iterate through each possible weight capacity
        for w in range(1, W + 1):
            # If the current item's weight is less than or equal to the current capacity
            if weights[i - 1] <= w:
                # Consider whether to include the current item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight exceeds the capacity, do not include it
                dp[i][w] = dp[i - 1][w]

    # The maximum value will be stored in dp[N][W]
    return dp[N][W]

# Input parsing
N, W = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

# Call the knapsack function and print the result
print(knapsack(N, W, weights, values))
