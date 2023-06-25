# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root: #if the root has no children, the depth to the lead node is 0
            return 0

        self.depth = float('inf') 
        self.dfs(root, 0) #send the root and the current depth as parameters

        return self.depth #return the minimum to the lead node

    def dfs(self, node, curDepth):
        if not node: #
            return 

        #if current node does not have any children
        if not node.left and not node.right: 
            self.depth = min(self.depth, (curDepth + 1))
            
        self.dfs(node.left, (curDepth + 1))
        self.dfs(node.right, (curDepth + 1))
        
                