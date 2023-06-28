class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        curr_counter = 0
        curr = nums[0]
        i = 0
        while i < len(nums) - counter:
            if nums[i] == curr:
                curr_counter += 1
                if curr_counter > 2:
                    self.bubbleSwap(nums, i, counter)
                    counter += 1
                    i -= 1
            else:
                curr = nums[i]
                curr_counter = 1
            i += 1
        return len(nums) - counter

    def bubbleSwap(self, nums, i, counter):
        for x in range(i, len(nums) - counter - 1):
            temp = nums[x]
            nums[x] = nums[x + 1]
            nums[x + 1] = temp
        nums[len(nums) - counter - 1] = None