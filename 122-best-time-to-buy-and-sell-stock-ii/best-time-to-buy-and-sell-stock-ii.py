class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [ -1 for j in range(2)]

        dp[0] = dp[1] = 0

        
        for ind in reversed(range(n)): 

            new_dp = [ -1 for j in range(2)]

            for buy in range(2):

                if buy == 0 :

                    ans = max(-prices[ind] + dp[1] , 0 + dp[0]) # buy or dont do any
                
                if buy == 1:

                    ans = max(prices[ind] + dp[0] , 0 + dp[1]) # sell or dont do any

                new_dp[buy] = ans
            
            dp = new_dp

        return dp[0]

