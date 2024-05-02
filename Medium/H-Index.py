class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        citations = citations[::-1]
        return sum(x < y for x, y in enumerate(citations))
        