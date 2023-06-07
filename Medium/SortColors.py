class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Bubble Sort
        length = len(nums)
        swapped = False
        for i in range(length - 1):
            for j in range(0, length - i - 1):
                if nums[j] > nums[j + 1]:
                    swapped = True
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            if not swapped:
                return
