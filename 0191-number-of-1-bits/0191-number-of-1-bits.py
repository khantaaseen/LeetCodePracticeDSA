class Solution:
    def hammingWeight(self, n: int) -> int:

        one = 0 

        while n != 0:
            one += n % 2
            n = n >> 1
        return one

