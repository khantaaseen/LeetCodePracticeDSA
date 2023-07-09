# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None


        currA = headA
        currB = headB

        while currA != currB:
            if currA:
                currA = currA.next
            else:
                currA = headB

            if currB:
                currB = currB.next
            else:
                currB = headA
        return currA

        
        # hashset = set()
        # curr = headA
        
        # while curr:
        #     hashset.add(curr)
        #     print("add to set: ", curr.val)
        #     curr = curr.next
        
        # curr = headB
        # while curr:
        #     if curr in hashset:
        #         print("curr.val in hashset", curr.val)
        #         return curr
        #     print("curr val: ", curr.val)
        #     curr = curr.next

        # return None




