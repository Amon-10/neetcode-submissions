class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1
        freq = list(sorted(res, key= lambda x: res[x], reverse=True))
        return freq[:k]

    