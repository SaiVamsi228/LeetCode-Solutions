# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_ll(curr,k):

            tail = curr

            prev = None

            while curr and k > 0:

                upcoming = curr.next

                curr.next = prev

                k -= 1

                prev = curr

                curr = upcoming

            return 

        temp = head

        prev = None

        my_head = None

        while temp :

            m_k = k - 1

            curr = temp

            while temp and m_k:

                temp = temp.next

                m_k -= 1
            
            if not temp:

                if prev:
                    
                    prev.next = curr

                break
            
            upcoming = temp.next
            
            m_k = k 

            reverse_ll(curr,m_k)

            if prev:

                prev.next = temp

            if not my_head:

                my_head = temp
            
            prev = curr

            temp = curr = upcoming

        
        return my_head
            


         

