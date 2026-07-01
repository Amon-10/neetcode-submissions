class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            newNum = 1
            for j in range(0, len(nums)):
                if j != i:
                    newNum *= nums[j]
            output.append(newNum)
        return output