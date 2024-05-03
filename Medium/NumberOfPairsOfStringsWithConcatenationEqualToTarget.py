class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if len(nums[i]) + len(nums[j]) != len(target):
                    continue
                if nums[i] + nums[j] == target:
                    res += 1
                if nums[j] + nums[i] == target:
                    res +=1
        return res