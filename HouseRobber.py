class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]
if __name__ == "__main__":
    # Input from the user
    nums = list(map(int, input().split(',')))

    # Calculate the maximum amount of money that can be robbed
    solution = Solution()
    maxMoney = solution.rob(nums)

    # Output the result
    print(maxMoney)