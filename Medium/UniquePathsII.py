class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mat = [[0]*n for i in range(m)]
        
        for i in range(m):
          if obstacleGrid[i][0] == 1:
            break
          mat[i][0] = 1
        for j in range(n):
          if obstacleGrid[0][j] == 1:
            break
          mat[0][j] = 1
        for i in range(1,m):
          for j in range(1,n):
              if obstacleGrid[i][j] == 1:
                mat[i][j] = 0
              else: 
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
          return 0
        return mat[m-1][n-1]