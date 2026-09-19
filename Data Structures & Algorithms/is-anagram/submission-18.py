class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsS = defaultdict(int)
        charsT = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            if char in charsS:
                charsS[char] += 1
            else:
                charsS[char] = 1
        
        for char in t:
            if char in charsT:
                charsT[char] += 1
            else:
                charsT[char] = 1
        
        if charsS == charsT:
            return True
        return False
