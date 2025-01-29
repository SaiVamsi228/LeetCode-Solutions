# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode(-1,None)

        temp = dummy_node

        carry = 0

        while l1 and l2:

            sm = l1.val + l2.val + carry

            carry = sm//10

            sm = sm % 10

            new_node = ListNode(sm,None)

            temp.next = new_node

            temp = temp.next

            l1 = l1.next

            l2 = l2.next

        
        while l1 :

            sm = l1.val + carry

            carry = sm//10

            sm = sm % 10

            new_node = ListNode(sm,None)

            temp.next = new_node

            temp = temp.next 

            l1 = l1.next
        
        while l2:

            sm = l2.val + carry

            carry = sm//10

            sm = sm % 10

            new_node = ListNode(sm,None)

            temp.next = new_node

            temp = temp.next 

            l2 = l2.next
        
        while carry:

            carry_node = ListNode(carry%10,None)

            temp.next = carry_node

            carry //= 10
        
        return dummy_node.next


