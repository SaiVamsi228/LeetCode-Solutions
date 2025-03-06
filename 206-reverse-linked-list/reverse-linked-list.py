# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLL(head,prev):

            if head and head.next == None :

                head.next = prev

                return head

            new_head =  reverseLL(head.next,head)

            head.next = prev

            return new_head


        if not head:

            return head

        temp = head
        
        return reverseLL(temp,None)


            


