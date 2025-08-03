class Solution:
    def jump(self, nums: List[int]) -> int:


        n = len(nums)

        def getMinSteps(ind):

            if ind >= n - 1:

                return 0
            
            if dp[ind] != -1:

                return dp[ind]
            
            mini_steps = float('inf')

            for k in range(1,nums[ind]+1):

                steps_req = 1 + getMinSteps(ind+k)

                mini_steps = min(mini_steps, steps_req)
            
            dp[ind] = mini_steps

            return dp[ind]
        
        dp = [-1 for i in range(n)]

        return getMinSteps(0)


