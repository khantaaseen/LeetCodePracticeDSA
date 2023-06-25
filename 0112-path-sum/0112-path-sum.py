# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        #O(N) time complexity because we have to go through every node to check total
        #O(N) memory complexity beacause we are using the height of the tree
        #best case memory complexity is O(logN) if this is balanced binary tree

        if not root: #base case, if there are no roots, it is not equal to any sum
            return False

        def dfs(node, total):

            if not node:
                return 

            total += node.val #add the value of the current node to our total
            if not node.left and not node.right: #executes if we are at a leaf node
            #if the total after coming to leaf code is == sum
                return total == targetSum 

            #this return statement will return true or false and get the true or false
            #between both sides of the tree   
            return (dfs(node.left, total) or 
                    dfs(node.right,total))

        #returning the current root, and the current total
        return dfs(root, 0)


