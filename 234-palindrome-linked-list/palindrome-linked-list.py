# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head

        prev = None

        cur = head

        upcoming = head.next

        while cur:

            upcoming  = cur.next

            cur.next = prev

            prev = cur

            cur = upcoming
        
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next 

            fast = fast.next.next

        newHead = self.reverseList(slow)

        firstHalfPt = head

        secondHalfPt = newHead

        while firstHalfPt and secondHalfPt:

            if firstHalfPt.val != secondHalfPt.val:

                self.reverseList(newHead)

                return False

            firstHalfPt = firstHalfPt.next

            secondHalfPt = secondHalfPt.next
        
        self.reverseList(newHead)

        return True
        
        