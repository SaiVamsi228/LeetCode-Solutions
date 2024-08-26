from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        hM = defaultdict(int)

        for num in nums:

            hM[num] += 1
        
        heap = []

        heapify(heap)

        for num,freq in hM.items():

            heappush(heap,(freq,-1 * num)) # -num because he wants
                                # to sort the numbers
                                # in decreasing order
                                # if the frequency of two 
                                # elements is same
        ans = []

        while heap:

            freq, num = heappop(heap)

            num =  -1 * num

            for i in range(freq):

                ans.append(num)
        
        return ans
        

