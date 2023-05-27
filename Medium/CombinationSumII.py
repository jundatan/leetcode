class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, res, [])
        return res

    def dfs(self, candidates, target, res, curr):
        if target < 0 or (target > 0 and not candidates):
            return
        if target == 0:
            if not curr in res:
                res.append(curr)
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates[i + 1:], target - candidates[i], res, curr + [candidates[i]])