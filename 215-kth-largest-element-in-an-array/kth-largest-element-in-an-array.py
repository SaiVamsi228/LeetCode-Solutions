from heapq import heappush, heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        mn_hp = []

        heapify(mn_hp)

        n = 0

        for num in nums:

            heappush(mn_hp,num)

            n += 1

            if n > k :

                heappop(mn_hp)

                n -= 1
        
        return heappop(mn_hp)
        
