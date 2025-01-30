# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        hash_set = set()

        temp = headA

        while temp:

            hash_set.add(temp)

            temp = temp.next
        
        temp = headB

        while temp:

            if temp in hash_set:

                return temp
            
            temp = temp.next
        
        return None