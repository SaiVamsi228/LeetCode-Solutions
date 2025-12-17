# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            
            return head
            
        arr = []

        temp = head

        while temp :

            arr.append(temp)

            temp = temp.next
        
        n = len(arr)

        left, right = 0, n - 1

        flag = True

        new_head = arr[left]

        while left < right:

            if flag:

                arr[left].next = arr[right]

                left += 1
            
                flag = False

                last = arr[right]
            
            else:

                arr[right].next = arr[left]

                right -= 1

                flag = True

                last = arr[left]

        last.next = None

        return new_head


        