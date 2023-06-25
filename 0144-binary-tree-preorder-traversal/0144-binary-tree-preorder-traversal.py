# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return None
        
        res = []
        stack = []
        curr = root
        #iterative solution

        while curr or stack:
            if curr:
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        
        return res


        #recursive
        # def preOrder(node):
        #     if not node:
        #         return

        #     arr.append(node.val)
        #     preOrder(node.left)
        #     preOrder(node.right)

        # preOrder(root)
            
        return res

