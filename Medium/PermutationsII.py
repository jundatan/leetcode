class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.recursive(nums, res, [], len(nums))
        return res
    
    def recursive(self, nums, res, curr, size):
        if len(curr) == size:
            if not curr in res:
                res.append(curr)
        temp = curr[::]
        temp_nums = nums[::]
        x = 0
        while x < len(nums):
            xx = nums[x]
            temp.append(xx)
            temp_nums.remove(xx)
            self.recursive(temp_nums, res, temp, size)
            if x + 1 < len(nums) and nums[x + 1] == nums[x]:
                x += 1
            temp = curr[::]
            temp_nums = nums[::]
            x += 1