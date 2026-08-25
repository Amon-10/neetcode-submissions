class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        
        for string in strs:
            seen[tuple(sorted(string))].append(string)
        return list(seen.values())
        
        
        