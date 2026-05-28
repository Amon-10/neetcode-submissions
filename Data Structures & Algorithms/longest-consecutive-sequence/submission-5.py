class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 1
        max_count = 1
        if not nums: return 0
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                continue
            elif sorted_nums[i] == sorted_nums[i - 1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1

        max_count = max(max_count, count)

        return max_count