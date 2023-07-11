# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node):
            if not node: return None

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
            
        dfs(root)

        #iterative solution
        # stack = [root]
        # res = []

        # while root or stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        #     if curr:
        #         res.append(curr.val)
        #     else:

        return res
