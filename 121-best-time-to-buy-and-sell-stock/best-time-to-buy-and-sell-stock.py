class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        buy_price = [0 for i in range(n)]

        sell_price = [0 for i in range(n)]

        best_buy_price = float('inf')

        best_sell_price = -float('inf')

        for i in range(n):

            best_buy_price = min(best_buy_price, prices[i])

            buy_price[i] = best_buy_price
        
        for i in reversed(range(n)):

            best_sell_price = max(best_sell_price, prices[i])

            sell_price[i] = best_sell_price
        
        
        mx_profit = 0

        for day in range(n):

            profit = sell_price[day] - buy_price[day]

            mx_profit = max(mx_profit,profit)
        
        return mx_profit

            