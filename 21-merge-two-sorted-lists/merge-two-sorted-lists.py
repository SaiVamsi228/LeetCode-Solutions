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
        
        
        new_head = ListNode(-1,None)

        temp = new_head

        while head1 and head2:

            if head1.val < head2.val :

                temp.next = head1

                head1 = head1.next
            
            else:

                temp.next = head2

                head2 = head2.next

            temp = temp.next
        
        while head1:

            temp.next = head1

            head1 = head1.next

            temp = temp.next
        
        while head2:

            temp.next = head2

            head2 = head2.next

            temp = temp.next

        return new_head.next