class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mid = n / 2
        res = 0
        for i in range(1, mid + 1):
            if n % i == 0:
                second = n / i
                if second == i:
                    res += 1
                else:
                    res += 2
        return res == 3