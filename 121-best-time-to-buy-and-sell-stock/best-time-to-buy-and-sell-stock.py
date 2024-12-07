class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]

        max_profit = 0

        n = len(prices)

        for i in range(1,n):

            cur_stock_price = prices[i]

            cur_profit = cur_stock_price - mini

            max_profit = max(cur_profit,max_profit)

            mini = min(mini,prices[i])
        
        return max_profit
