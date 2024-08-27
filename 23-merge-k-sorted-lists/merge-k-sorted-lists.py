# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(-1)

        temp = head
        
        minHeap = []
        
        heapify(minHeap)
        
        n = len(lists)

        for i in range(n):
            
            if lists[i]:
                
                heappush(minHeap,(lists[i].val,i))
            
        while minHeap:
            
            ele,i = heappop(minHeap)
            
            temp.next = lists[i]

            temp = lists[i]
            
            if lists[i].next:
                
                lists[i] = lists[i].next
                
                heappush(minHeap,(lists[i].val,i))               
            
        
        return head.next