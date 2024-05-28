# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head
        
        prev2 = None

        prev = head

        cur = head.next

        while prev:

            prev.next = prev2

            prev2 = prev 

            prev = cur

            if not cur:

                break

            cur = cur.next
        
        return prev2
        


        