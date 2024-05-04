class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    print(i, j)
                    a = self.iterate(i, j, land)
                    res.append(a)
        return res

    def iterate(self, x, y, land):
        m = len(land)
        n = len(land[0])
        x1 = 0
        y1 = 0
        for i in range(x, m):
            if land[i][y] == 0:
                break
            for j in range(y, n):
                if land[i][j] == 1:
                    if i > x1:
                        x1 = i
                    if j > y1:
                        y1 = j
                    land[i][j] = 0
                else:
                    break
        return [x, y, x1, y1]
        