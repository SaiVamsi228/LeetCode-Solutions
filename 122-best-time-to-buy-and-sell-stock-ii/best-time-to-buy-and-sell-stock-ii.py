class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        if n == 1 :

            return 0
        
        max_profit = 0

        maxi, mini = prices[0], prices[0]

        cur_profit = maxi - mini

        for i in range(1,n):

            if prices[i] < maxi :

                max_profit += cur_profit

                mini = maxi = prices[i]
            
            elif prices[i] >= maxi :

                maxi = max(maxi,prices[i])

            cur_profit = maxi - mini
        
        # if the stock price is increasing only

        if cur_profit > 0:

            max_profit += cur_profit
        
        return max_profit



