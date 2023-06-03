class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 1
        for x in nums:
            if x == res:
                res += 1
        return res