class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        res =[]
        for i in range(len(grid)-2):
            temp = []
            for j in range(len(grid)-2):
                arr = [row[j:j+3] for row in grid[i:i+3]]
                maximum_flat = sum(arr, [])
                maximum_value = max(maximum_flat)
                temp.append(maximum_value)
            res.append(temp)
        return res