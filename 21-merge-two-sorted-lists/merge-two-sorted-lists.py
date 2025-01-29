# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = list1

        head2 = list2

        if not head1 :

            return head2
        
        if not head2:

            return head1
        
        merged_list = []

        temp1, temp2 = head1, head2

        while temp1:

            merged_list.append(temp1.val)

            temp1 = temp1.next
        
        while temp2 :

            merged_list.append(temp2.val)

            temp2 = temp2.next
        
        merged_list.sort()

        i = 0

        n = len(merged_list)

        new_head = ListNode(-1,None)

        temp = new_head

        while i < n :

            new_node = ListNode(merged_list[i],None)

            temp.next = new_node

            temp = new_node

            i += 1
        
        return new_head.next


