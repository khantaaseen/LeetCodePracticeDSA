# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return None

        res = []
        
        def dfs(root, stack):

            if not root:
                return

            stack.append(str(root.val))
            
            if not root.left and not root.right: #means we've come to a leaf node
                res.append("->".join(stack))
            
            if root.left:
                dfs(root.left, stack)

            if root.right:
                dfs(root.right, stack)

            stack.pop()

        dfs(root, [])

        return res
                    
