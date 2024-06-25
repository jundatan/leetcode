class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        while True:
            if tickets[k] == 0:
                break
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[i] > 0:
                    tickets[i] -= 1
                    res += 1
        return res
