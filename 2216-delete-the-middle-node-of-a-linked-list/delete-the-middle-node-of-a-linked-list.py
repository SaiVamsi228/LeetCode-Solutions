import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return None

        n = -1

        temp = head

        while temp:

            n += 1

            temp = temp.next
            
        middleNode = math.ceil(n/2)

        temp = head

        currPos = 0

        while currPos < middleNode - 1:

            temp = temp.next

            currPos += 1

        
        temp.next = temp.next.next

        return head
