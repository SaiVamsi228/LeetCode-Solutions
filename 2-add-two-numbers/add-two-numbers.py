# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = l1

        temp2 = l2

        carry = 0

        dummyNode = ListNode(-1)

        temp = dummyNode

        while temp1 or temp2 or carry :

            newNodeVal = 0
            
            if temp1:
                
                newNodeVal += temp1.val 

                temp1 = temp1.next
            
            if temp2:
                
                newNodeVal += temp2.val 
                
                temp2 = temp2.next


            if carry :

                newNodeVal += carry

                carry = 0

            if newNodeVal >=10:
                
                carry = newNodeVal // 10

                newNodeVal = newNodeVal % 10

            temp.next = ListNode(newNodeVal)

            temp = temp.next

        if carry :

            temp.next = ListNode(carry)

        
        newHead = dummyNode.next

        return newHead
        