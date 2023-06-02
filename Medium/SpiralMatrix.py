class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        rows = len(matrix)
        if not matrix:
            return matrix
        col = len(matrix[0])
        length = col * rows - 1
        count = 0
        x = 0
        y = 0
        end_row = rows - 1
        end_col = col - 1
        start_row = 0
        start_col = 0
        down = False
        right = True
        left = False
        up = False
        while True:
            res.append(matrix[x][y])
            count += 1
            if count > length:
                break
            if y == end_col and right:
                start_row += 1
                right = False
                left = False
                up = False
                down = True
                x += 1
            elif x == end_row and down:
                end_col -= 1
                right = False
                left = True
                up = False
                down = False
                y -= 1
            elif y == start_col and left:
                end_row -= 1
                right = False
                left = False
                up = True
                down = False
                x -= 1
            elif x == start_row and up:
                start_col += 1
                right = True
                left = False
                up = False
                down = False
                y += 1 
            elif right:
                y += 1
            elif left:
                y -= 1
            elif up:
                x -= 1
            elif down:
                x += 1
        return res