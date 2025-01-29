# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:

            return head

        def rev_list(head,prev):

            if not head.next:

                head.next = prev

                return head
            
            new_head = rev_list(head.next,head)

            head.next = prev

            return new_head
        
        return rev_list(head,None)
        

        