class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        orderedNums = sorted(nums)
        consec = []
        count = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(orderedNums)):
            if orderedNums[i] == orderedNums[i - 1]:
                continue
            elif orderedNums[i] == orderedNums[i - 1] + 1:
                count += 1
            else:
                consec.append(count)
                count = 1
        consec.append(count)
        return max(consec)
