# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hashMap = {}

        temp = head

        ind = 0

        while temp:

            if temp in hashMap:

                return temp
            
            hashMap[temp] = ind

            ind += 1

            temp = temp.next
        
        return None