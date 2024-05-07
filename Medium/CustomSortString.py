class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        idx = {char: index for index, char in enumerate(order)}

        sortedS = sorted(s, key = lambda x : idx.get(x, float('inf')))

        return ''.join(sortedS)
        