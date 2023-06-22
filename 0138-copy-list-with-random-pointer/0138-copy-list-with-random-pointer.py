"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dupe = {None: None}

        curr = head

        #first pass of linked list
        #add values of og linked list to hashmap
        while curr:
            copy = Node(curr.val)
            dupe[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = dupe[curr]
            copy.next = dupe[curr.next]
            copy.random = dupe[curr.random]
            curr = curr.next
        

        return dupe[head]