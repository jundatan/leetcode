class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.heap = {}
        for i in range(len(nums)):
            if nums[i] in self.heap:
                self.heap[nums[i]].append(i)
            else:
                self.heap[nums[i]] = [i]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        targetList = self.heap.get(target)
        randInt = random.randrange(len(targetList))
        return targetList[randInt]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)