from heapq import heapify, heappush, heappop
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        maxHeap = []

        heapify(maxHeap)

        n = 0

        ans = []

        for num in arr:

            heappush(maxHeap,(-(abs(num-x)),-num))

            n += 1

            if n > k :

                heappop(maxHeap)

                n -= 1        
        
        while maxHeap:

            ans.append(- heappop(maxHeap)[1])

        ans.sort()

        return ans

