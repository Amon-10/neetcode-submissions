class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        most_frequent_element = Counter(nums).most_common(k)
        key_with_most_frequent_element = [key for key, count in most_frequent_element]
        return key_with_most_frequent_element