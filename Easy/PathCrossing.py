class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = [(0,0)]
        x, y = 0, 0
        for i in path:
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1
            else:
                x -= 1
            if (x,y) in visited:
                return True
            else:
                visited.append((x,y))
        print(visited)
        return False