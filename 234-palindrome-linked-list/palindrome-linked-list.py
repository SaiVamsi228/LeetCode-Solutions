# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head

        fast = head

        firstHalf = []

        n = 0

        while fast and fast.next:

            firstHalf.append(str(slow.val))

            n += 1

            slow = slow.next 

            fast = fast.next.next

        secondHalf = []

        while slow :

            secondHalf.append(str(slow.val))

            n += 1

            slow = slow.next
        
        firstHalf = "".join(firstHalf)

        secondHalf = "".join(secondHalf)

        if n%2 == 0:

            return firstHalf == secondHalf[::-1]
        
        return firstHalf == (secondHalf[::-1])[:-1]
        