class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)

        dp = [ -1 for i in range(n+1)]

        dp[1] = nums[0]

        for i in range(2,n+1):

            rob = nums[i-1]

            if i-2 > 0:

                rob = nums[i-1] + dp[i-2]
            
            notRob = 0 + dp[i-1]
            
            dp[i] = max(rob, notRob)
        
        return dp[n]