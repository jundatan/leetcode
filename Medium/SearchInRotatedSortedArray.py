class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        res = self.recurse(low, high, nums, target)
        return res
    
    def recurse(self, low, high, nums, target):
        mid = (high + low) / 2
        if low > high:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target and nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
            return self.recurse(low, high, nums, target)
        else:
            if nums[high] >= target and nums[mid] <= target:
                    low = mid + 1
            else:
                    high = mid - 1
            return self.recurse(low, high, nums, target)