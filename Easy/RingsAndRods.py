class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        heap = {
            'R' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'B' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'G' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
        count = 0
        for i in range(0, len(rings), 2):
            color = rings[i: i+1]
            rod = int(rings[i+1:i+2])
            if color in heap:
                heap[color][rod] += 1
        for i in range(10):
            if heap['R'][i] > 0 and heap['B'][i] > 0 and heap['G'][i] > 0:
                count += 1
        return count