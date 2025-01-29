# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def get_length(head):

            n = 0

            temp = head

            while temp:

                n += 1

                temp = temp.next
            
            return n
        
        if head.next == None and n == 1:

            return None

        N = get_length(head)

        if N-n == 0:

            return head.next

        temp = head

        for i in range(1,N-n):

            temp = temp.next
        
        temp.next = temp.next.next

        return head

