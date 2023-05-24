class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, len(matrix) - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        i, j = 0, 0
        while True:
            if i >= len(matrix):
                break
            elif j < len(matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            else:
                i += 1
                j = i