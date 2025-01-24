# tabulation approach
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)
        
        dp = [-float('inf') for buy in range(2)]

        dp[0] = dp[1] = 0

        cur_dp = [-float('inf') for i in range(2)]

        for day in reversed(range(n)):

            for buy in range(2):

                if buy == 0:

                    buy_profit = -prices[day] + dp[1]

                    buy_on_other = dp[buy]  

                    cur_dp[buy] = max(buy_profit, buy_on_other)
                
                elif buy == 1:

                    sell_profit = prices[day] 

                    sell_on_other = dp[buy]

                    cur_dp[buy] = max(sell_profit, sell_on_other)
            
            dp = cur_dp

        return dp[0]



