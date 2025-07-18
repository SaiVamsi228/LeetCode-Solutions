class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        l_prod = 1

        r_prod = 1

        n = len(nums)

        mx = float('-inf')

        for i in range(n):

            l_prod *= nums[i]

            r_prod *= nums[n-i-1]

            mx = max(mx,l_prod)

            mx = max(mx, r_prod)

            if nums[i] == 0:

                l_prod = 1
            
            if nums[n-i-1] == 0:

                r_prod = 1
        
        return mx


