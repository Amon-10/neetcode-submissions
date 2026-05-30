class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sort_nums = sorted(nums)
        
        for i in range(len(nums)):
            seen = {}
            fixed = sort_nums[i]
            target = -fixed
            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                diff = target - sort_nums[j]
                if diff in seen:
                    res.add((fixed, diff, sort_nums[j]))
                seen[sort_nums[j]] = j
        return list(res)