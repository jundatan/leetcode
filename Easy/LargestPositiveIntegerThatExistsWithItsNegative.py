class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        maximum = -1
        for i in nums:
            if i < 0:
                x = i * -1
            else:
                x = i
            if i in s:
                maximum = maximum if x < maximum else x
            else:
                s.add(i * -1)
        return maximum