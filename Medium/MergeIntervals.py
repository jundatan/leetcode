class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for index in range(1, len(intervals)):
            curr = res.pop()
            start = intervals[index][0]
            end = intervals[index][1]
            if curr[1] < start:
                res.append(curr)
                res.append(intervals[index])
            else:
                res.append([min(curr[0], start), max(curr[1], end)])
        return res