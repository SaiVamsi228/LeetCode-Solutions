# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = []

        n2 = []

        temp = l1

        while temp :

            n1.append(str(temp.val))

            temp = temp.next
        
        temp = l2

        while temp :

            n2.append(str(temp.val))

            temp = temp.next
        
        num1 = int(("".join(n1))[::-1])

        num2 = int(("".join(n2))[::-1])

        ans = str(num1 + num2)

        ans = ans[::-1]

        i = 0

        n = len(ans)

        new_head = ListNode(-1,None)

        temp = new_head

        while i < n:

            new_node = ListNode(int(ans[i]), None)

            temp.next = new_node

            temp = temp.next

            i += 1
        
        return new_head.next


