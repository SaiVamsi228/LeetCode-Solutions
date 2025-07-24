# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head :

            return head

        length = 0

        temp = head

        while temp:

            length += 1

            temp = temp.next
        
        k = k % length 
        
        if k == 0 :

            return head

        slow = head

        fast = head

        for i in range(k):

            fast = fast.next
        
        before = None

        while fast :
            
            before = slow

            slow = slow.next 

            fast = fast.next
        
        before.next = None

        new_head = slow

        while slow.next:

            slow = slow.next
        
        slow.next = head

        return new_head