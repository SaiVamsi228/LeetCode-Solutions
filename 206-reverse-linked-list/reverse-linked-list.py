# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def revList(self,head):

        if not head or not head.next:

            return head
        
        new_head = self.revList(head.next)

        front = head.next
        
        front.next = head

        head.next = None

        return new_head


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.revList(head)
        


        