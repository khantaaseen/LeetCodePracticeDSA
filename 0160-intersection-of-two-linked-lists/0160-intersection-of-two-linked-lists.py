# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None


        #essentially this algorithm assigns two pointers to run through each of the linked lists
        #if one of the curr nodes is null before the other curr node we begin curr node at head
        #of the opposite list and same for the other node, doing this will cause each curr to be 
        #at the same node if there is an intersection because the pointers will begin to match 
        #up in speed

        #two pointer approach similar to floydes tortoise and hare algorithm
        currA = headA
        currB = headB

        while currA != currB: #if values are same, intersect found and return either val
            if currA: #while not null keep going
                currA = currA.next
            else: #when this becomes null reassign pointer to beginning of second list
                currA = headB

            if currB: #while not null keep going 
                currB = currB.next
            else: #when becomes null assign this to other list until they are equal
                currB = headA
        return currA #when equal you can return either list val

        
        # hashset = set()
        # curr = headA
        
        # while curr:
        #     hashset.add(curr)
        #     curr = curr.next
        
        # curr = headB
        # while curr:
        #     if curr in hashset:
        #         return curr
        #     curr = curr.next

        # return None




