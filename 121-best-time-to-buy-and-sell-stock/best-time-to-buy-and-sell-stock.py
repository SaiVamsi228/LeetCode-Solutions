class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        def getMaxProfit(day,buy):

            if day == n:

                return 0
            
            if dp[day][buy] != - float('inf'):

                return dp[day][buy]

            if buy == 0:

                buy_profit = -prices[day] + getMaxProfit(day+1, 1)

                buy_on_other = getMaxProfit(day+1,buy)  

                dp[day][buy] = max(buy_profit, buy_on_other)
            
            elif buy == 1:

                sell_profit = prices[day] 

                sell_on_other = getMaxProfit(day+1, buy)

                dp[day][buy] = max(sell_profit, sell_on_other)
            
            return dp[day][buy]
        
        n = len(prices)

        dp = [[-float('inf') for buy in range(2)]for day in range(n)]

        return getMaxProfit(0,0)