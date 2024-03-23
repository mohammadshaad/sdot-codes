def find_longest_increasing_subsequence(sequence):
    if not sequence:
        return 0

    n = len(sequence)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    sequence = list(map(int, input().split(",")))
    longest_increasing_subsequence_length = find_longest_increasing_subsequence(sequence)
    print(longest_increasing_subsequence_length)