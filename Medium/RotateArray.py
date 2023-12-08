class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0:
          return
        if len(nums) < k:
          nums[:] = self.rotate(nums, len(nums))
          nums[:] = self.rotate(nums,k-len(nums))
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums