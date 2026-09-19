class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxH = 0
        totalW = 0

        while l < r:
            if height[l] <= height[r]:
                maxH = max(maxH, height[l])
                totalW += maxH - height[l]
                l += 1
            else:
                maxH = max(maxH, height[r])
                totalW += maxH - height[r]
                r -= 1
        
        return totalW