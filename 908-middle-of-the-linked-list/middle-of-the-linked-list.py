# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = slow = head

        if not slow or not slow.next:

            return head

        while fast != None and fast.next:

            slow = slow.next

            fast = fast.next.next
        
        return slow
