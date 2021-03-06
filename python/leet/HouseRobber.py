class Solution(object):
    def rob(self, nums):
        size = len(nums)

        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums)

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        maxRob = dp[size - 1]

        return maxRob
        