# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        listSet = set()

        temp = head

        while temp :

            if temp in listSet:

                return True

            listSet.add(temp)

            temp = temp.next
        
        return False