from heapq import heapify, heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []

        heapify(maxHeap)

        n = 0

        for point in points:

            x, y = point

            dist = sqrt(x**2 + y**2)

            heappush(maxHeap,(-dist,point))

            n += 1

            if n > k :

                heappop(maxHeap)

                n -= 1

        ans = []
        
        while maxHeap:

            ans.append(heappop(maxHeap)[1])
        

        return ans


