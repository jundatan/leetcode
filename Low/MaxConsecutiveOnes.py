class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                count += 1
            else:
                count = 0
            if count > max_count:
                max_count = count
        return max_count