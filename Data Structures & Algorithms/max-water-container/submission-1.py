class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        volume = 1
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                base = j - i
                if heights[i] >= heights[j]:
                    volume = heights[j] * base
                    max_v = max(max_v, volume)
                elif heights[j] > heights[i]:
                    volume = heights[i] * base
                    max_v = max(max_v, volume)
        return max_v

