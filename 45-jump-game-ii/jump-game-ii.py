class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0

        n = len(nums)

        l = r = 0

        jumps = 0

        while r < n-1:

            farthest = 0

            for ind in range(l,r+1):

                farthest = max(ind + nums[ind], farthest)
            
            jumps += 1

            l = r + 1

            r = farthest
        
        return jumps

            