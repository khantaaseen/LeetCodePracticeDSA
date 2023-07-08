class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hashset = set()

        for i in nums:
            if i in hashset:
                return i
            else:
                hashset.add(i)
        return None


        #or floydes algorithm of fast and slow pointers

        # slow, fast = 0, 0

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break 

        # slow2 = 0
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        #     if slow == slow2:
        #         return slow
            

