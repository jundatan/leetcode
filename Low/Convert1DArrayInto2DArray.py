class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if m * n != len(original):
            return []
        for i in range(m):
            res.append(original[i*n:i*n + n])
        return res