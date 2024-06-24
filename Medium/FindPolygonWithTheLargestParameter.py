class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = -1
        count = 0
        maxi = -1
        for i in nums:
            if i < res and res != -1 and count >= 2:
                res += i
                maxi = res
            elif count >= 1:
                res += i
            else:
                res = i
            count += 1
        return maxi