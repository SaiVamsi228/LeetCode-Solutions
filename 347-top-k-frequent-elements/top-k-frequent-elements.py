from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = []

        freq = Counter(nums)

        n = 0

        for num, frq in freq.items():

            heappush(hp,(frq,num))

            n += 1

            if n > k:

                heappop(hp)

                n -= 1
        
        ans = []

        while hp :

            ans.append(heappop(hp)[1])
        
        return ans


