class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        deduct = 0
        res = 0
        while happiness and k > 0:
            level = happiness.pop() + deduct
            if level <= 0:
                break
            res += level
            deduct -= 1
            k -= 1
        return res