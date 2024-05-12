class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * 3
        for i in nums:
            temp = dp[:]
            for j in range(3):
                temp[((i+dp[j])%3)] = max(temp[(i+dp[j])%3], i+dp[j])
            dp = temp
        return dp[0]