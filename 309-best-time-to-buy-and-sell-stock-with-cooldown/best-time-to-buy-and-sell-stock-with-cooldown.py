class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        dp = [ [ [ -1 for day in range(n+1)] for buy in range(2)] for coolTime in range(2)]

        for buy in range(2):

            for coolTime in range(2) :

                dp[coolTime][buy][n] = 0
        
        for day in reversed(range(n)):

            for buy in reversed(range(2)):

                for coolTime in reversed(range(2)) :

                    if buy == 0: # buy or leave
                
                        # before buying check cooling time

                        if coolTime == 0:

                            profit = max( -prices[day] + dp[0][1][day+1] , 0 + dp[0][0][day+1])
                        
                        else:

                            profit = 0 + dp[coolTime - 1][0][day+1]

                    if buy == 1: #sell or leave
                        
                        profit = max(prices[day] + dp[1][0][day+1] , 0 + dp[0][1][day+1])

                    dp[coolTime][buy][day] = profit

    
        return dp[0][0][0]
            
