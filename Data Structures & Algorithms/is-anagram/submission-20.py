class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = defaultdict(int)
        freqT = defaultdict(int)

        for char in s:
            if char in freqS:
                freqS[char] += 1
            else:
                freqS[char] = 1
        
        for char in t:
            if char in freqT:
                freqT[char] += 1
            else:
                freqT[char] = 1

        if freqT != freqS:
            return False
        return True