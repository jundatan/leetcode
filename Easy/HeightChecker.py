class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        temp = heights[:]
        temp.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                res += 1
        return res