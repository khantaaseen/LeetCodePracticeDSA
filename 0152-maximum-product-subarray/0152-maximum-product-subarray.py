class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums) #highest value in nums
        curMin, curMax = 1, 1
        
        for n in nums: #iterate through each number in nums
            if n == 0:
                curMin, curMax = 1, 1
                continue 
            temp = curMax * n 
            curMax = max(curMin * n, curMax * n, n )
            curMin = min(curMin * n, temp, n)
            res = max(res, curMin, curMax)

        return res



