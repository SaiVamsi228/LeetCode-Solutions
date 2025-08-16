class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def getMaxMoney(ind):

            if ind >= n :

                return 0
            
            if ind in dp:

                return dp[ind]

            rob_money = nums[ind] + getMaxMoney(ind+2)

            rob_others = getMaxMoney(ind+1)

            dp[ind] = max(rob_money,rob_others)

            return dp[ind]
        
        n = len(nums)

        dp = {}
        
        return getMaxMoney(0)