class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        min_length = min(len(s1), len(s2), len(s3))
        minimum = 0
        for i in range(min_length):
            if s1[i] == s2[i] and s1[i] == s3[i]:
                minimum += 1
            else:
                break
        if minimum == 0:
            return -1
        res = len(s1)-minimum
        res += len(s2)-minimum
        res += len(s3)-minimum
        return res
