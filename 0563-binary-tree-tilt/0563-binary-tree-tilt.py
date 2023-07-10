# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(node):
            if not node:
                return 0
            
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)

            self.res += abs(leftsum - rightsum)
            
            return node.val + leftsum + rightsum
        
        dfs(root)

        return self.res