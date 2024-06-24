class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        pos = 0
        neg = 1
        for i in nums:
            if i < 0:
                res[neg] = i
                neg += 2
            else:
                res[pos] = i
                pos += 2
        return res 