#Algo code referenced from: https://leetcode.com/problems/3sum/solutions/3491162/100-solution-explained/
class Solution(object):
    def threeSum(self, nums):
        finalList = []
        nums.sort()
        print(nums)
        for x in range(len(nums)):
            left = x + 1
            right = len(nums) - 1
            if x > 0 and nums[x] == nums[x - 1]:
                    continue
            while left < right:
                sum = nums[x] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    curr = [nums[x], nums[left], nums[right]]
                    finalList.append(curr)
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return finalList

