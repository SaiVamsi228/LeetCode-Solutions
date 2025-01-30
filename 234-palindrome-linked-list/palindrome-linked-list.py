# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:

            return True
        
        slow = head

        fast = head

        st = []

        while fast and fast.next:

            st.append(slow.val)

            slow = slow.next

            fast = fast.next.next

        if fast and fast.next == None:

            slow = slow.next

        while slow:

            if slow.val == st[-1]:

                st.pop()
            
            else:

                return False
            
            slow = slow.next
        
        
        return True


