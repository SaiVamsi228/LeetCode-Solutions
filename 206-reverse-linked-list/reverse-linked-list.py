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

        curr = head     

        upcoming = head.next

        while curr:

            curr.next = prev

            prev = curr

            if upcoming == None:

                break
            
            else:

                curr = upcoming
                
                upcoming = curr.next
        
        return curr