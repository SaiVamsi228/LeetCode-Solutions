# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head

        h1 = head

        h2 = head.next

        curr1 = h1

        curr2 = h2

        while curr1 and curr2:
            
            curr1.next = curr1.next.next

            if curr2.next:
                
                curr2.next = curr2.next.next

            prev = curr1

            curr1 = curr1.next

            curr2 = curr2.next
        
        if curr1:
            
            curr1.next = h2
        
        else:

            prev.next = h2

        return h1
        

