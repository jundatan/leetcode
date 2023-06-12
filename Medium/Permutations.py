class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        size = len(nums)
        self.recursive(nums, res, [], size)
        return res

    def recursive(self, nums, res, curr, size):
        if len(curr) == size:
            res.append(curr)
        temp_nums = nums[::]
        temp_curr = curr[::]
        for x in range(len(nums)):
            temp_curr.append(nums[x])
            temp_nums.remove(nums[x])
            self.recursive(temp_nums, res, temp_curr, size)
            temp_nums = nums[::]
            temp_curr = curr[::]