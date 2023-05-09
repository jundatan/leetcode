class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i, x in enumerate(nums):
            if i > 0 and nums[i - 1] == x:
                continue
            for y in range(i + 1, len(nums)):
                if y > i + 1 and nums[y - 1] == nums[y]:
                    continue
                left = y + 1
                right = len(nums) - 1
                while left < right:
                    fourSum = x + nums[y] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        res.append([x, nums[y], nums[left] ,nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
        return res