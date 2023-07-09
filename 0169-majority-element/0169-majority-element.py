class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        res = 0
        maxC = 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxC:
                res = n
            maxC = max(maxC, count[n])
        
        return res