# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:

            return None
        
        slow = fast = head

        # taking fast n steps forward so that it let us know to stop at n steps before
        
        for i in range(n):

            fast = fast.next
        
        # if the first node is to be removed when n == N

        if fast == None:

            return slow.next
        
        while fast and fast.next:

            slow = slow.next

            fast = fast.next
        
        slow.next = slow.next.next

        return head
