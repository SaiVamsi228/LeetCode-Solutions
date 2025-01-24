# TABULATION APPROACH
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        n = len(nums)

        dp = [[-float('inf') for start in range(2)] for ind in range(n+1)]
        
        dp[1][0] = nums[0]

        dp[1][1] = max(0,nums[0])

        for ind in range(2,n+1):

            for start in range(2):

                if start == 0:

                    start_new_sub_arr = nums[ind-1] + dp[ind-1][1]

                    start_at_other = dp[ind-1][start]

                    dp[ind][start] = max(start_new_sub_arr, start_at_other)
                
                elif start == 1:

                    end_cur_sub_arr = 0
                    
                    end_at_other = nums[ind-1] + dp[ind-1][start]

                    dp[ind][start] = max(end_cur_sub_arr, end_at_other)
        
        return dp[n][0]
                