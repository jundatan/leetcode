class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                if i + 3 < len(s):
                    i += 3
                    count += 1
                    continue
                else:
                    count += 1
                    break
            i += 1
        return count