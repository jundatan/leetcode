class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.recursive(nums, res, [])
        return res
    
    def recursive(self, nums, res, curr):
        curr.sort()
        if not curr in res:
            res.append(curr)
        temp = curr[::]
        for x in range(len(nums)):
            temp.append(nums[x])
            self.recursive(nums[x + 1:], res, temp)
            temp = curr[::]