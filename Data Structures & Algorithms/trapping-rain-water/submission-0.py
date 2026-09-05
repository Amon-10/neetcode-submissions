class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        total = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                if height[left] < leftMax:
                    total += leftMax - height[left]
                    left += 1
                else:
                    left += 1

            else:
                rightMax = max(rightMax, height[right])
                if height[right] < rightMax:
                    total += rightMax - height[right]
                    right -= 1
                else:
                    right -= 1
        
        return total