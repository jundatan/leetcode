class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        heap = {}
        for i in range(len(s) - 9):
            curr = s[i : i + 10]
            heap[curr] = heap.get(curr, 0) + 1
        return [x for x, y in heap.items() if y > 1]