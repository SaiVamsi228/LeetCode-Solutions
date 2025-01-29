# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next and n == 1:

            return None

        temp1 = temp2 = head

        for i in range(n):

            temp1 = temp1.next
        
        # if the first node is to be removed when n == N
        if temp1 == None :

            return temp2.next

        while temp1.next != None:

            temp1 = temp1.next

            temp2 = temp2.next
        
        
        temp2.next = temp2.next.next

        return head

