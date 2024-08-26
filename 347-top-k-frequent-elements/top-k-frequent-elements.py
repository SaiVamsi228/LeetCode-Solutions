from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hM = defaultdict(int)

        for num in nums:

            hM[num] += 1
        
        minHeap = []

        heapify(minHeap)

        n = 0
        
        for num,freq in hM.items():

            heappush(minHeap,(freq,num))

            n += 1
            
        while n > k:

            heappop(minHeap)

            n -= 1
        
        ans = []

        while minHeap:

            ans.append(heappop(minHeap)[1])

        return ans
