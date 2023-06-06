class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        start = newInterval[0]
        end = newInterval[1]
        res = []
        count = 0
        if intervals == []:
            return [newInterval]
        if end < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if start > intervals[len(intervals) - 1][1]:
            intervals.append(newInterval)
            return intervals
        for index in range(len(intervals)):
            interv = intervals[index]
            if start >= interv[0] and start <= interv[1]:
                res.append([min(start, interv[0]), max(end, interv[1])])
                count += 1
                break
            elif start < interv[0]:
                res.append(newInterval)
                break
            else:
                res.append(interv)
                count += 1
        for index in range(count, len(intervals)):
            interv = intervals[index]
            curr = res.pop()
            if interv[0] <= curr[1] and interv[0] >= curr[0]:
                res.append([min(curr[0], interv[0]), max(curr[1], interv[1])])
            else:
                res.append(curr)
                res.append(interv)
        return res
                