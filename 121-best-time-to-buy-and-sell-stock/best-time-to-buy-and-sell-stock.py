# tabulation approach
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)
        
        dp = [[-float('inf') for buy in range(2)] for day in range(n+1)]

        dp[n][0] = dp[n][1] = 0

        for day in reversed(range(n)):

            for buy in range(2):

                if buy == 0:

                    buy_profit = -prices[day] + dp[day+1][1]

                    buy_on_other = dp[day+1][buy]  

                    dp[day][buy] = max(buy_profit, buy_on_other)
                
                elif buy == 1:

                    sell_profit = prices[day] 

                    sell_on_other = dp[day+1][buy]

                    dp[day][buy] = max(sell_profit, sell_on_other)

        return dp[0][0]



