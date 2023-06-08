class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        self.recursive(nums, res, [])
        return res
    
    def recursive(self, nums, res, curr):
        temp_curr = curr[:]
        for x in range(len(nums)):
            val = nums[x]
            temp_curr.append(val)
            res.append(temp_curr)
            self.recursive(nums[x + 1:], res, temp_curr)
            temp_curr = curr[:]