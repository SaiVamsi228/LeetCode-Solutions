# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = list1

        temp2 = list2

        dummyNode = ListNode(-1)

        temp = dummyNode

        while temp1 and temp2:

            if temp1.val < temp2.val:

                temp.next = temp1

                temp1 = temp1.next
            
            else:
                temp.next = temp2

                temp2 = temp2.next
            
            temp = temp.next
        
        if temp1 is not None:

            temp.next = temp1
        
        if temp2 is not None:

            temp.next = temp2
        
        newHead = dummyNode.next

        return newHead

        