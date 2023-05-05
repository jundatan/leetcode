class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            minHeight = min(height[left], height[right])
            length = right - left
            area = minHeight * length
            if area > maxArea:
                maxArea = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea