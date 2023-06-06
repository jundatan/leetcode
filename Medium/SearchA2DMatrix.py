class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        length = len(matrix)
        start = 0
        end = length - 1

        if len(matrix) == 1 and target in matrix[0]:
            return True
        while start <= end:
            mid = (start + end) / 2
            last = len(matrix[mid]) - 1
            if target in matrix[mid]:
                return True
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][last]:
                start = mid + 1
            else:
                return False
        return False
        