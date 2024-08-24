import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = 0

        minHeap = [] 

        for num in nums:

            heapq.heappush(minHeap,num)

            n += 1

            if n > k :

                heapq.heappop(minHeap)

                n -= 1
        
        return heapq.heappop(minHeap)