class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)

        dp = [[ [-1 for ind in range(n+1)] for buy in range(2)] for trans in range(k+1+1)]

        for ind in range(n+1):

            for trans in range(k+1+1):

                for buy in range(2):

                    if ind == n :

                        dp[trans][buy][ind] = 0
                    
                    if trans == 3 :

                        dp[trans][buy][ind] = 0

        for ind in reversed(range(n)):

            for trans in reversed(range(k+1)):

                for buy in range(2):

                    if buy == 0: # buy or skip
                    
                        profit = max(-prices[ind] + dp[trans+1][1][ind + 1] , 0 + dp[trans][0][ind+1])
                    
                    elif buy == 1: # sell or skip

                        profit = max( prices[ind] + dp[trans][0][ind + 1] , 0 + dp[trans][1][ind + 1])

                    
                    dp[trans][buy][ind] = profit


        return dp[0][0][0]