# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) < 1:
            return None

        def BuildTree(nums, start, end):

            if start > end:
                return None

            index = start

            for i in range(start + 1, end + 1):
                if nums[i] > nums[index]:
                    index = i
            
            root = TreeNode(nums[index])

            root.left = BuildTree(nums, start, index - 1)
            root.right = BuildTree(nums, index + 1, end)

            return root

        return (BuildTree(nums, 0, len(nums) - 1))


