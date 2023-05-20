class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                mid_start = mid
                mid_end = mid
                if mid + 1 < len(nums) and nums[mid + 1] == target:
                    while mid_end + 1 < len(nums) and nums[mid_end + 1] == target:
                        mid_end += 1
                if mid - 1 >= 0 and nums[mid - 1] == target:
                    while mid_start - 1 >= 0 and nums[mid_start - 1] == target:
                        mid_start -= 1
                return [mid_start, mid_end]
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [-1, -1]