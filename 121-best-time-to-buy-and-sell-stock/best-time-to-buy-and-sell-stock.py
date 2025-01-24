class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_buy_price = float('inf')

        max_profit = 0

        n = len(prices)

        for cur_day in range(n):

            best_buy_price = min(prices[cur_day], best_buy_price)

            max_profit = max(max_profit, prices[cur_day] - best_buy_price)
        
        return max_profit