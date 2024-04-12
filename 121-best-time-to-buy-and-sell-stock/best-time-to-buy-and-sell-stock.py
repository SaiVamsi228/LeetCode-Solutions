class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        min_price = prices[0]

        max_pro = 0

        for i in range(n):

            min_price = min(prices[i],min_price)

            max_pro = max(max_pro, prices[i] - min_price)
        
        return max_pro
