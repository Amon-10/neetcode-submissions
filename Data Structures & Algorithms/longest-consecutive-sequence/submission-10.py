class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 1
        max_count = 1
        if len(nums) == 0: return 0
        for i in range(1, len(nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                count += 1
            elif sorted_nums[i] == sorted_nums[i - 1]:
                continue
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count