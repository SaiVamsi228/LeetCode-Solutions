# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def get_length(head):

            n = 0

            temp = head

            while temp:

                n += 1

                temp = temp.next
            
            return n

        if not head or not head.next:

            return head
        
        n = get_length(head)

        k = k % n

        if k == 0:

            return head
        
        temp = head

        while temp.next:

            temp = temp.next

        temp.next = head

        while n - k:

            temp = temp.next
        
            k += 1
        
        new_head = temp.next

        temp.next = None

        return new_head

