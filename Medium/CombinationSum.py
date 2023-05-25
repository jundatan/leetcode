class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.recurse(candidates, target, res, [])
        return res

    def recurse(self, candidates, target, result, curr_list):
        if target == 0:
            result.append(curr_list)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            self.recurse(candidates[i:], target - candidates[i], result, curr_list + [candidates[i]])