class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [ [-1 for prev_ind in range(n+1)] for ind in range(n+1)]

        for prev_ind in range(-1,n):

            dp[n][prev_ind+1] = 0

        for ind in reversed(range(n)):

            for prev_ind in reversed(range(-1,ind)):

                take = 0
            
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:

                    take = 1 + dp[ind+1][ind+1]
                
                notTake = 0 + dp[ind+1][prev_ind+1]

                dp[ind][prev_ind+1] =  max(take,notTake)
        
        return dp[0][0]
