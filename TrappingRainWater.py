def trap_rain_water(heights):
    n = len(heights)
    if n <= 2:
        return 0  # No water can be trapped with less than 3 bars

    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height of bar to the left of each bar
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Calculate the maximum height of bar to the right of each bar
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    water_trapped = 0
    # Calculate the amount of water trapped at each bar
    for i in range(n):
        min_height = min(left_max[i], right_max[i])
        water_trapped += min_height - heights[i]

    return water_trapped


if __name__ == "__main__":
    heights = list(map(int, input().split()))
    
    # Compute the amount of water trapped after raining
    trapped_water = trap_rain_water(heights)

    # Output the result
    print(trapped_water)