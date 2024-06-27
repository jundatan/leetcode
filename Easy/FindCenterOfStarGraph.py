class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges[1][0] in edges[0]:
            return edges[1][0]
        return edges[1][1]