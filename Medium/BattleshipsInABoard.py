class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        visited = []
        ships = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if board[i][j] == 'X':
                    board[i][j] = '.'
                    a = j + 1
                    while a < n and board[i][a] == 'X':
                        board[i][a] = '.'
                        visited.append((i, a))
                        a += 1
                    b = i + 1
                    while b < m and board[b][j] == 'X':
                        board[b][j] = '.'
                        visited.append((b, j))
                        b += 1
                    ships += 1
        return ships