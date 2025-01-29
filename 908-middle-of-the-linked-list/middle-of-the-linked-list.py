# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = 0

        temp = head

        while temp :

            n += 1

            temp = temp.next
        
        temp = head

        middle = (n//2) + 1

        for i in range(1,middle):

            temp = temp.next
        
        return temp
