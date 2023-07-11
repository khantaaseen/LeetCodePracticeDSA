# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #iterative inorder traversal
        # stack = []
        # res = []

        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     res.append(root.val)
        #     root = root.right
        # return res

        #recursive inorder traversal

        res = []

        def inOrder(node):
            if not node: return None

            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return res






