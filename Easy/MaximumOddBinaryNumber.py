class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')-1
        n = len(s)
        res = ''
        for i in range(n-1):
            if ones:
                res += '1'
                ones -= 1
            else:
                res += '0'
        res += '1'
        return res