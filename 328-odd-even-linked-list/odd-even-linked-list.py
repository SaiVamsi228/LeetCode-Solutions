# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head
        
        cur = head.next

        prev = head

        queue = []

        even = True

        while cur:

            if even :
                
                upcoming = cur.next

                queue.append(cur)

                cur.next = None

                prev.next = upcoming

                cur = upcoming

                even = False
            
            else:

                prev = cur

                cur = cur.next 

                even = True
        
        while queue:

            prev.next = queue.pop(0)

            prev = prev.next
        
        return head

