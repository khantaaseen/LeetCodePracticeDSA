# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # res = []

        # def dfs(node):
        #     if not node: return None

        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
            
        # dfs(root)

        #iterative solution
        stack = [root]
        visited = [False]
        res = []

        while stack:
            curr = stack.pop()
            v = visited.pop()
            
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return res
            






