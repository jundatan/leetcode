import random
class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.dictionary = {}
        self.length = n - len(blacklist)
        for i in blacklist:
            self.dictionary[i] = -1
        last = n - 1
        for i in blacklist:
            if i < self.length:
                while last in self.dictionary:
                    last -= 1
                self.dictionary[i] = last
                last -= 1

    def pick(self):
        """
        :rtype: int
        """
        randomInt = random.randint(0, self.length - 1)
        return self.dictionary.get(randomInt,randomInt)

# Ref from https://leetcode.com/problems/random-pick-with-blacklist/solutions/2128394/python-solution-faster-than-97-79-using-hashmap-with-detailed-explanation
# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()