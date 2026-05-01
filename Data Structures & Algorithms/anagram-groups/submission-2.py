class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort = sorted(strs)
        output = []
        seen = [False] * len(strs)
        for i in range(len(strs)):
            if seen[i]: continue
            ana = []
            ana.append(strs[i])
            seen[i] = True
            for j in range(i + 1, len(strs)):
                if not seen[j] and sorted(strs[i]) == sorted(strs[j]):
                    ana.append(strs[j])
                    seen[j] = True
            output.append(ana)
        return output