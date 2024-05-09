class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = [float('inf')] + arr + [float('inf')]
        n = len(arr)
        res = 0
        while n > 3:
            x = min(arr)
            idx = arr.index(x)

            if arr[idx+1]<arr[idx-1]:
                res += arr[idx+1] * arr[idx]
            else:
                res += arr[idx-1] * arr[idx]
            arr.remove(x)
            n = len(arr)
        return res

#Ref from https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/1510611/greedy-approach-97-faster-well-explained/