class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.recursive(n, k, 1, [], res)
        return res

    def recursive(self, n, k, no, curr, res):
        if len(curr) == k:
            res.append(curr[::])
            return
        for x in range(no, n + 1):
            curr.append(x)
            self.recursive(n, k, x + 1, curr, res)
            curr.pop()