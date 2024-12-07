class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)

        def getMaxProfit(ind, buy, trans):

            if trans == -1:

                return 0

            if ind == n :

                return 0
            
            if dp[trans][buy][ind] != -1:

                return dp[trans][buy][ind]
        
            if buy == 0: # buy or skip

                if trans >= 1:

                    profit = max(-prices[ind] + getMaxProfit(ind + 1, 1, trans - 1 ) , 0 + getMaxProfit(ind+1, 0, trans))

                else:

                    profit = 0 
            
            elif buy == 1: # sell or skip

                profit = max( prices[ind] + getMaxProfit(ind + 1 , 0, trans) , 0 + getMaxProfit(ind + 1, 1 , trans))

            
            dp[trans][buy][ind] = profit

            return profit
        
        dp = [[ [-1 for ind in range(n+1)] for buy in range(2)] for trans in range(2+1)]

        return getMaxProfit(0,0,2)

                


