# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()
        res = []
        q.append(root)


        while q:
            height = len(q)
            level = 0
            for i in range(height):
                node = q.popleft()
                level += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelavg = level / height
            res.append(levelavg)
        return res

            
