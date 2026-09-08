class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxV = 0

        while left < right:
            if heights[left] <= heights[right]:
                area = (right - left) * heights[left]
                maxV = max(maxV, area)
                left += 1
            elif heights[left] > heights[right]:
                area = (right - left) * heights[right]
                maxV = max(maxV, area)
                right -= 1
        return maxV
            