class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        sm = 0
        n = len(nums)
        for i in range(n):

            mx = nums[i]

            mn = nums[i]

            for j in range(i,n):

                mn = min(mn, nums[j])

                mx = max(mx, nums[j])
            
                sm += (mx - mn)
        
        return sm
