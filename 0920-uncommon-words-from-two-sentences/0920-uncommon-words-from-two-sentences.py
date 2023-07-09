class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        frq = {}
        res = []

        for x in s1.split(" "):
            if x in frq:
                frq[x] += 1
            else:
                frq[x] = 1
            
        for y in s2.split(" "):
            if y in frq:
                frq[y] += 1
            else:
                frq[y] = 1

        for i in frq:
            if frq[i] == 1:
                res.append(i)
        return res


        