class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        def getMaxProfit(day,buy,coolingTime):

            if day == n :

                return 0
            
            if dp[coolingTime][buy][day] != -1:

                return dp[coolingTime][buy][day]
            
            if buy == 0: # buy or leave
                
                # before buying check cooling time

                if coolingTime == 0:

                    profit = max( -prices[day] + getMaxProfit(day + 1, 1, 0), 0 + getMaxProfit(day + 1, 0, 0 ))
                
                else:

                    profit = 0 + getMaxProfit(day +1 , 0, coolingTime - 1)

            if buy == 1: #sell or leave
                
                profit = max(prices[day] + getMaxProfit(day + 1, 0, 1 ) , 0 + getMaxProfit(day+1, 1, 0))
            
            dp[coolingTime][buy][day] = profit

            return profit
        
        dp = [ [ [ -1 for day in range(n+1)] for buy in range(2+1)] for coolTime in range(2)]
    
        return getMaxProfit(0,0,0)
            
