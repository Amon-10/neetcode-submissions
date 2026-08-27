class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        running = 1
        for i in range(len(nums)):
            left[i] = running
            running *= nums[i]
        
        right = [1] * len(nums)
        rRunning = 1
        for j in range(len(nums) - 1, - 1, - 1):
            right[j] = rRunning
            rRunning *= nums[j]
        
        combined = [1] * len(nums)
        for k in range(len(nums)):
            combined[k] = right[k] * left[k]
        return combined
            