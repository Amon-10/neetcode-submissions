class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        v = []
        for i in reversed(s):
            if i.isalnum():
                t.append(i.lower())
        
        for j in s:
            if j.isalnum():
                v.append(j.lower())
        
        return t == v


        
