class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        return res
    def decode(self, i: str) -> List[str]:
        res = []
        s = 0

        while s < len(i):
            j = s
            while i[j] != '#':
                j+= 1
            length = int(i[s:j])
            s = j + 1
            j = s + length
            res.append(i[s:j])
            s = j
        
        return res
