# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tortoise =  head

        hare = head

        while hare.next and hare.next.next:

            tortoise = tortoise.next

            hare = hare.next.next
        
        if hare.next:

            return tortoise.next
        
        return tortoise




        
            
