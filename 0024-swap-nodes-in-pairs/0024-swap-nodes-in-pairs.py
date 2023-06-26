# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        dummy = ListNode(0)
        curr = dummy
        curr.next = head

        while curr.next and curr.next.next:
            temp1 = curr.next
            temp2 = curr.next.next
            temp3 = curr.next.next.next
            
            curr.next = temp2
            curr.next.next = temp1
            curr.next.next.next = temp3
            curr = curr.next.next
            
        return dummy.next
