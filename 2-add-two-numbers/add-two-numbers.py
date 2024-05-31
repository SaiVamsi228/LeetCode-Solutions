# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        
        prev = None
        
        temp = head

        while temp:
            
            upcoming = temp.next
            
            temp.next = prev
            
            prev = temp
            
            temp = upcoming

        
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = l1

        temp2 = l2

        carry = 0

        dummyNode = ListNode(-1)

        temp = dummyNode

        while temp1 and temp2 :

            newNodeVal = temp1.val + temp2.val + carry

            carry = 0

            if newNodeVal >=10:
                
                carry = newNodeVal // 10

                newNodeVal = newNodeVal % 10

            temp.next = ListNode(newNodeVal)

            temp = temp.next

            temp1 = temp1.next

            temp2 = temp2.next
        
        while temp1:

            newNodeVal = temp1.val + carry
            
            carry = 0

            if newNodeVal >=10:
                
                carry = newNodeVal // 10

                newNodeVal = newNodeVal % 10

            temp.next = ListNode(newNodeVal)

            temp = temp.next

            temp1 = temp1.next
        
        while temp2:

            newNodeVal = temp2.val + carry

            carry = 0

            if newNodeVal >=10:
                
                carry = newNodeVal // 10

                newNodeVal = newNodeVal % 10

            temp.next = ListNode(newNodeVal)

            temp = temp.next

            temp2 = temp2.next


        if carry :

            temp.next = ListNode(carry)

        
        newHead = dummyNode.next

        return newHead
        