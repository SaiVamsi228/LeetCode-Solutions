# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hash_set = set()

        temp = head

        while temp:

            if temp in hash_set:

                return temp
            
            else:

                hash_set.add(temp)
            
            temp = temp.next
        
        return None