# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        arr = []

        temp = head

        n = 0

        while temp:

            arr.append(temp.val)

            n += 1

            temp = temp.next
        
        ind = 0

        while ind + k - 1 < n:

            i = ind 

            j = i + k - 1

            while i <= j :

                arr[i], arr[j] = arr[j], arr[i]
            
                i += 1

                j -= 1
            
            ind += k

        temp = head

        i = 0

        while temp:

            temp.val = arr[i]

            i += 1

            temp = temp.next
        
        return head

         

