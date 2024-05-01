import copy
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        squares = 0
        startingRow = None
        startingCol = None
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    squares += 1
                if grid[i][j] == 1:
                    startingRow = i
                    startingCol = j
        return self.recurse(startingRow, startingCol, 0, squares + 1, grid)
    def recurse(self, i, j, k, total, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == -1 or grid[i][j] == 3:
            return 0
        if grid[i][j] == 2:
            if k == total:
                return 1
            else:
                return 0
        newGrid = copy.deepcopy(grid)
        newGrid[i][j] = 3
        sum = self.recurse(i + 1, j, k + 1, total, newGrid) + self.recurse(i - 1, j, k + 1, total, newGrid) + self.recurse(i, j + 1, k + 1, total, newGrid) + self.recurse(i, j - 1, k + 1, total, newGrid)
        return sum