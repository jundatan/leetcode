class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        heap = {}
        length = len(word1)
        for i in range(length):
            wordofw1 = word1[i]
            if wordofw1 in heap:
                heap[wordofw1] += 1
            else:
                heap[wordofw1] = 1
        for i in range(length):
            wordofw2 = word2[i]
            if wordofw2 in heap:
                heap[wordofw2] -= 1
            else:
                heap[wordofw2] = -1
        for i in heap.values():
            if i > 3 or i < -3:
                return False
        return True