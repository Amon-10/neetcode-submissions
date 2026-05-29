class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_nums = sorted(numbers)
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if new_nums[i] == new_nums[j]:
                    continue
                elif new_nums[i] + new_nums[j] == target:
                    return [i + 1, j + 1]