# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse_list(head):

            prev = None

            curr = head

            upcoming = head.next

            while curr:

                curr.next = prev

                prev = curr

                curr = upcoming

                if curr != None:

                    upcoming = curr.next
            
            return prev

        if not head or not head.next:

            return True

        slow = head

        fast = head


        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next
        
        new_head = reverse_list(slow)


        temp1, temp2 = head, new_head

        while temp1 and temp2 :

            if temp1.val != temp2.val:

                return False
            
            temp1 = temp1.next

            temp2 = temp2.next

        
        return True


