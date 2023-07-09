class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        cTOw = {}
        wTOc = {}

        for c, w in zip(pattern, words):
            if c in cTOw and cTOw[c] != w:
                return False
            
            if w in wTOc and wTOc[w] != c:
                return False
            
            cTOw[c] = w
            wTOc[w] = c

        return True
    




