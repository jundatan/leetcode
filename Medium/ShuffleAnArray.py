import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.original
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        temp = self.original[:]
        random.shuffle(temp)
        return temp
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()