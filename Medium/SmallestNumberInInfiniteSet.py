# Ref from: https://leetcode.com/problems/smallest-number-in-infinite-set/solutions/3453958/super-logic-with-heap-approach/
class SmallestInfiniteSet(object):
    
    def __init__(self):
        self.infiniteList = []
        self.smallest = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.infiniteList:
            return heapq.heappop(self.infiniteList)
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not num in self.infiniteList:
            if num < self.smallest:
                heapq.heappush(self.infiniteList, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)