class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [0 for i in range(n)]

        for ind in reversed(range(n)):

            if ind + 2 < n :

                rob_money = nums[ind] + dp[ind+2]
            
            else:

                rob_money = nums[ind] + 0

            if ind + 1 < n :

                rob_others = dp[ind+1]
            
            else:

                rob_others = 0

            dp[ind] = max(rob_money,rob_others)
        
        return dp[0]