class Solution(object):
    def threeSumClosest(self, nums, target):
        closestSum = None
        nums.sort()
        for i, x in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summ = x + nums[left] + nums[right]
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else:
                    return target
                if closestSum == None:
                    closestSum = summ
                differenceClosest = abs(target - closestSum)
                differenceSumm = abs(target - summ)
                if differenceSumm < differenceClosest:
                    closestSum = summ
        return closestSum