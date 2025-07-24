# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseLL(node,k):

            before = None

            new_head = None

            new_tail = node

            temp = node

            while temp and k > 0:

                upcoming = temp.next

                temp.next = before

                before = temp

                temp = upcoming

                k -= 1
            
            new_head = before

            return new_head, new_tail
        
        
        dummy = ListNode(-1)

        temp = head

        before = dummy

        while temp:

            curr = temp

            m_k = k - 1

            while temp and m_k > 0:

                temp = temp.next 

                m_k = m_k - 1
            
            if not temp:

                if before :

                    before.next = curr

                break
            
            upcoming = temp.next # store the upcoming segment

            temp.next = None # break the segment

            new_head, new_tail = reverseLL(curr,k)

            if before:

                before.next = new_head
            
            before = new_tail

            temp = upcoming
        
        return dummy.next
