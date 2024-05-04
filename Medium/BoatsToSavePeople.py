class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        start = len(people) - 1
        end = 0
        count = 0
        while start >= end:
            personA = people[start]
            if personA == limit:
                count += 1
                start -= 1
            else:
                personB = people[end]
                if personA + personB <= limit and start != end:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    start -= 1
                    count += 1
        return count