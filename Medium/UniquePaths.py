class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[1]*n for i in range(m)]
        mat[0][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[m-1][n-1]