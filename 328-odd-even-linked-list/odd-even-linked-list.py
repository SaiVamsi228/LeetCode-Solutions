# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head

        arr = []

        temp = head

        n = 0

        while temp:

            arr.append(temp.val)

            n += 1

            temp = temp.next
        
        oddPt = 0

        evenPt = 1

        odd = True

        temp = head


        while temp:

            if oddPt < n: #odd

                temp.val = arr[oddPt]

                oddPt += 2
            
            else:

                temp.val = arr[evenPt]

                evenPt +=2
            
            temp = temp.next

        return head

        

            
