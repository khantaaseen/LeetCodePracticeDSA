class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1 = s1.split(" ")
        s2 = s2.split(" ")

        frq = {}
        res = []

        for x in s1:
            if x in frq:
                frq[x] += 1
            else:
                frq[x] = 1
            
        for y in s2:
            if y in frq:
                frq[y] += 1
            else:
                frq[y] = 1

        for i in frq:
            if frq[i] == 1:
                res.append(i)
        return res


        