# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head
        
        newHead = head.next

        even = False

        cur = head

        while cur.next:

            if even:

                upcoming = cur.next

                cur.next = cur.next.next

                cur = upcoming

                even = False


            else:

                upcoming = cur.next

                cur.next = cur.next.next

                prev = cur

                cur = upcoming

                even = True

        
        if even == False : 

            cur.next = newHead
        
        else:

            prev.next = newHead

        
        return head
    