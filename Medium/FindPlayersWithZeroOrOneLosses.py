class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = {}
        for i in matches:
            if not i[1] in heap:
                heap[i[1]] = 1
            elif i[1] in heap:
                heap[i[1]] += 1
            if not i[0] in heap:
                heap[i[0]] = 0
        res = [[], []]
        for x,y in heap.items():
            if y == 0:
                res[0].append(x)
            if y == 1:
                res[1].append(x)
        res[0].sort()
        res[1].sort()
        return res