# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse_ll(head,k):

            prev = None

            curr = head

            while curr and k > 0:

                upcoming = curr.next

                curr.next = prev

                k -= 1

                prev = curr

                curr = upcoming
            
            new_head = prev

            return new_head
        
        slow = head

        fast = head

        prev = None

        k = 1

        while fast and fast.next:

            prev = slow

            slow = slow.next 

            k += 1

            fast = fast.next.next

        if fast:

            # it is odd length

            temp2 = slow.next

            temp1 = reverse_ll(head,k)

            temp1 = temp1.next
        
        else:

            # it is of even length

            # so slow is one step ahead lets use prev

            temp2 = slow

            temp1 = reverse_ll(head,k - 1)
        
        while temp1 and temp2:

            if temp1.val != temp2.val:

                return False
            
            temp1 = temp1.next

            temp2 = temp2.next
        
        return True


            



