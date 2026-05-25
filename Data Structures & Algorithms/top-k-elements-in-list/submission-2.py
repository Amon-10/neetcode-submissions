class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_most_frequent = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for m in range(k):
            highest_key = max(counts, key=counts.get)
            k_most_frequent.append(highest_key)
            del counts[highest_key]
            
        return k_most_frequent