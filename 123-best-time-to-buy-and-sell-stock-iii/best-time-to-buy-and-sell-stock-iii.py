class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)

        dp = [[0 for buy in range(2)] for trans in range(3+1)]

        for ind in reversed(range(n)):

            new_dp = [[-1 for buy in range(2)] for trans in range(3+1)]

            for trans in reversed(range(3)):

                for buy in range(2):

                    if buy == 0: # buy or skip
                    
                        profit = max(-prices[ind] + dp[trans+1][1] , 0 + dp[trans][0])
                    
                    elif buy == 1: # sell or skip

                        profit = max( prices[ind] + dp[trans][0] , 0 + dp[trans][1])

                    
                    new_dp[trans][buy] = profit
            
            dp = new_dp


        return dp[0][0]

                


