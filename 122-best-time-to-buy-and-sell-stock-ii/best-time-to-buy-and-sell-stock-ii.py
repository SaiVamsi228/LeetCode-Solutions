class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        if n == 1 :

            return 0

        # to compute [6,1,3,2,4,7] it automatically calculates profit on the ending day

        prices = prices + [0] 

        n = len(prices)
        
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
        
        return max_profit



