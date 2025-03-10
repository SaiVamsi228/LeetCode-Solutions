# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head :

            return head

        temp = head

        n = 0

        while temp.next:

            n += 1

            temp = temp.next
        
        n += 1
        

        k = k % n 

        if k == 0 :

            return head
        
        temp.next = head

        steps = n - k

        while steps > 0 :

            temp = temp.next

            steps -= 1
        
        head = temp.next

        temp.next = None

        return head
