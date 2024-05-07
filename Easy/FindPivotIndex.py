class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums[1:])
        for i in range(0, len(nums)):
            if left == right:
                return i
            left += nums[i]
            if i + 1 == len(nums):
                right = 0
            else:
                right -= nums[i+1]
        return -1