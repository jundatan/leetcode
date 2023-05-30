class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        while rows:
            row = rows.pop(0)
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        while cols:
            col = cols.pop(0)
            for i in range(len(matrix)):
                matrix[i][col] = 0