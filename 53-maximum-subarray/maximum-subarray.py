from sys import maxsize
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far = -maxsize

        max_ending_here = 0

        for num in nums:

            max_ending_here += num

            if max_ending_here > max_so_far:

                max_so_far = max_ending_here
            
            if max_ending_here < 0:

                max_ending_here = 0 #No point in carrying neg sum start new subarray from next ele
        
        return max_so_far
        
