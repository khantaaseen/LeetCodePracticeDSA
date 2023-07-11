# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = len(queue)
            order = []
            for i in range(level):
                node = queue.popleft()
                level += 1
                if node:
                    order.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if order:
                res.append(order)
        return res

