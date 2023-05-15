#Ref from: https://leetcode.com/problems/next-permutation/solutions/3473399/beats-100-full-explanation-in-steps/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        firstPointer = -1
        secondPointer = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstPointer = i
                break
        if firstPointer == -1:
            return self.reverse(nums, 0)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[firstPointer]:
                secondPointer = i
                break
        temp = nums[firstPointer]
        nums[firstPointer] = nums[secondPointer]
        nums[secondPointer] = temp
        self.reverse(nums, firstPointer + 1)

    def reverse(self, nums, start):
        nums[start:len(nums)] = nums[start:len(nums)][::-1]