class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        heap = {}
        while nums:
            smallest = nums.pop(0)
            biggest = nums.pop()
            avg = (smallest + biggest)
            avg = avg / 2.0
            if not avg in heap:
                heap[avg] = 1
        return len(heap)