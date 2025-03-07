# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        d1 = headA

        d2 = headB

        while d1 and d2:

            if d1 == d2:

                return d1
            
            d1 = d1.next

            d2 = d2.next

            if d1 == None and d2 == None:

                return None # no intersection point
            
            elif d1 == None:

                d1 = headB
            
            elif d2 == None:

                d2 = headA
        



