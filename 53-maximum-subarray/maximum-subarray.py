class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # nums = [-2,1,-3,4,-1,2,1,-5,4]
        # o/p : 6

        def getMaxSubarrSum(n,start):

          if n == 1:

            if start == 0:

                return nums[0]
            
            else:
                
                return max(0,nums[0])

          if dp[n][start] != -float('inf'):

            return dp[n][start]

          if start == 0:

            start_new_sub_arr = nums[n-1] + getMaxSubarrSum(n-1,1)

            start_at_other = getMaxSubarrSum(n-1,start)

            dp[n][start] = max(start_new_sub_arr, start_at_other)
          
          elif start == 1:

            end_cur_sub_arr = 0
            
            end_at_other = nums[n-1] + getMaxSubarrSum(n-1,start)

            dp[n][start] = max(end_cur_sub_arr, end_at_other)
          
          return dp[n][start]

        n = len(nums)

        dp = [[-float('inf') for start in range(2)] for ind in range(n+1)]

        return getMaxSubarrSum(n,0)