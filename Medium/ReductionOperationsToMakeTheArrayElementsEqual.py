class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        lowest = nums[0]
        count = 0
        curr = None
        res = 0
        for i in range(n-1,-1,-1):
            if curr == nums[i]:
                count += 1
                continue
            curr = nums[i]
            res += count
            count += 1
        return res