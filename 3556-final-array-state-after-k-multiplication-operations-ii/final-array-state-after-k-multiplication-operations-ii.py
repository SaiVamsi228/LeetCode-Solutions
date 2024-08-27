from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:  # optimization for multiplier == 1
            return nums
        
        n, MOD, mx = len(nums), 10**9 + 7, max(nums)
        minHeap = [(num, ind) for ind, num in enumerate(nums)]
        heapify(minHeap)

        # Apply modifications using the heap
        while k > 0:
            num, ind = heappop(minHeap)
            nums[ind] = num * multiplier
            heappush(minHeap, (nums[ind], ind))
            k -= 1

            if nums[ind] > mx:  # If we exceed the original max, break
                break
        
        if k == 0:  # If no more operations are left
            for num, ind in minHeap:
                nums[ind] = num % MOD
            return nums
        
        # Full cycle optimizations
        full_cycles = k // n
        left_over = k % n
        y = pow(multiplier, full_cycles, MOD)  # Efficient power calculation
        
        for _ in range(left_over):
            num, ind = heappop(minHeap)
            nums[ind] = (num * multiplier) % MOD

        return [(x * y) % MOD for x in nums]
