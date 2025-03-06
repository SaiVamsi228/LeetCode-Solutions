# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)

        temp1 = l1

        temp2 = l2

        temp = dummy

        carry = 0

        while temp1 and temp2:

            sm = temp1.val + temp2.val + carry
            
            carry = sm//10

            sm %= 10

            new_node = ListNode(sm)

            temp.next = new_node

            temp = temp.next

            temp1 = temp1.next

            temp2 = temp2.next

        while temp1:

            sm = temp1.val + carry
            
            carry = sm//10

            sm %= 10

            new_node = ListNode(sm)

            temp.next = new_node

            temp = temp.next

            temp1 = temp1.next

        while temp2:

            sm = temp2.val + carry
            
            carry = sm//10

            sm %= 10

            new_node = ListNode(sm)

            temp.next = new_node

            temp = temp.next

            temp2 = temp2.next
        

        

        
        if carry:

            new_carry_node = ListNode(carry)

            temp.next = new_carry_node

        
        return dummy.next

