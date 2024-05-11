class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_val = n*n
        res = 0
        for i in range(1, n):
            for j in range(i+1, n):
                p = i*i + j*j
                if p > max_val:
                    break
                if pow(p, 0.5)%1==0:
                    res += 2
        return res