class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l = 0
        i , r = len(nums) - 1, len(nums) - 1
        res = [0] * len(nums)

        while i >= 0: 
            if abs(nums[r]) > abs(nums[l]):
                res[i] = nums[r] * nums[r]
                r -= 1
            else:
                res[i] = nums[l] * nums[l]
                l += 1
            i -= 1
        return res