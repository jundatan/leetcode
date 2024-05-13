class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        if n == 1:
            return 'p'
        for i in range(n-2):
            res += 'p'
        if n%2==0:
            res +='p'+'x'
        else:
            res += 'z'+'x'
        return res
        