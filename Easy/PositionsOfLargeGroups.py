class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        prev = ''
        count = 0
        start = 0
        res = []
        for i in range(len(s)):
            if s[i] != prev:
                if count >= 3:
                    res.append([start, i - 1])
                start = i
                prev = s[i]
                count = 1
            else:
                count += 1
        if count >= 3:
            res.append([start, len(s)-1])
        return res