#Ref from: https://leetcode.com/problems/spiral-matrix-ii/solutions/3506760/day-405-brute-better-optimal-3-liner-0ms-100-python-java-c-explained/
class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        self.spiral(matrix, 0, n - 1, 0, n - 1, 1)
        return matrix

    def spiral(self, matrix, top, bottom, left, right, num):
        if top > bottom or left > right:
            return
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        for i in range(top + 1, bottom + 1):
            matrix[i][right] = num
            num += 1
        if top < bottom and left < right:
            for i in range(right - 1, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = num
                num += 1
        self.spiral(matrix, top + 1, bottom - 1, left + 1, right - 1, num)