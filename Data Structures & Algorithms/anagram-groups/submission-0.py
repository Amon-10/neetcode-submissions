class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sorted_i = tuple(sorted(i))
            res[sorted_i].append(i)
    
        return list(res.values())
            
