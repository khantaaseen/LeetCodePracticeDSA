# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root: #if the tree is empty, nothing to change
            return None

        #decides on what side of the tree we should search in
        if key < root.val: #if key is smaller, search in left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: #if key is larger, serach in right subtree
            root.right = self.deleteNode(root.right, key)
        else: #at this moment we have found the key in the BST

            if not root.left: #if there is no left child, the deleted node becomes right
                return root.right 
            elif not root.right: #if theres no right child, deleted node becomes left
                return root.left

            #after deleting and if there are children nodes
            #go down the right subtree and find the minimum in that right tree
            curr = root.right #since we are looking for min in right tree, curr = right 
            while curr.left: #while there are left childred (for min keep going left)
                curr = curr.left #keep going left for min
            root.val = curr.val #after you have found the min this becomes our curr value
            #to get rid of dupe node after deleting, find this node and delete it
            root.right = self.deleteNode(root.right, root.val)
        return root







