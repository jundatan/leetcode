class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        y = len(nums) - 1
        res = 0
        while x <= y:
            if x == y:
                res += nums[x]
                break
            s = str(nums[x]) + str(nums[y])
            num = int(s)
            res += num
            x += 1
            y -= 1
        return res