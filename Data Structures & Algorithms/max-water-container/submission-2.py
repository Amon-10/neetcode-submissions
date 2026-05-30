class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        area = 1
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                base = j - i
                area = min(heights[i], heights[j]) * base
                max_v = max(max_v, area)
                
        return max_v

