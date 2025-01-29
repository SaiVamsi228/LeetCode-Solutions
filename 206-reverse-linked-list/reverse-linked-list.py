# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:

            return head
        
        if not head.next:

            return head
        
        temp = head

        ele = []

        while temp :

            ele.append(temp.val)

            temp = temp.next

        temp = head

        n = len(ele)

        for i in range(n-1,-1,-1):
            
            temp.val = ele[i]

            temp = temp.next
        
        return head


