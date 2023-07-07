# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:
            #if both of the vals are greater then search in right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #if both of the val are less, search in left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            #if the values are in different subtrees, the root is the LCA
            else:
                return curr