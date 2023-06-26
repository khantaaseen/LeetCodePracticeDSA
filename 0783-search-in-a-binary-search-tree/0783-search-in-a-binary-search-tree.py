# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None


        if root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        
        if root.val > val:
            return self.searchBST(root.left, val)
        
        # stack = []
        # res = []
        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         if curr.val == val:
        #             return (curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        # return None

