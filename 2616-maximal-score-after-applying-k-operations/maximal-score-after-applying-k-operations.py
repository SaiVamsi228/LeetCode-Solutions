import math
from heapq import heappush, heappop
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        score = 0

        hp = [] 

        heapify(hp)

        for i, num in enumerate(nums):

            heappush(hp,(-num,i))
        
        while k :

            mx, ind = heappop(hp)

            mx *= -1

            score += mx

            mx = math.ceil(mx/3)

            heappush(hp,(-mx,ind))

            k -= 1
        
        return score