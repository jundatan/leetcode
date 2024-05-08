class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        temp = []
        for i in range(len(score)):
            temp.append((i ,score[i]))
        temp = sorted(temp, key=lambda x : x[1])
        n = len(temp) - 1
        for i in range(n , -1, -1):
            if i == n:
                score[temp[i][0]] = "Gold Medal"
            elif i == n - 1:
                score[temp[i][0]] = "Silver Medal"
            elif i == n - 2:
                score[temp[i][0]] = "Bronze Medal"
            else:
                score[temp[i][0]] = (str) (len(temp) - i)
        
        return score