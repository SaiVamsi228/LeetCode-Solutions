class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [ [-1 for _ in range(n+1)] for j in range(2)]

        dp[0][n] = dp[1][n] = 0

        
        for ind in reversed(range(n)): # ind went from 0 to n-1 but ofc initialization is taken place for ind == n
            for buy in range(2):

                if buy == 0 :

                    ans = max(-prices[ind] + dp[1][ind+1] , 0 + dp[0][ind+1]) # buy or dont do any
                
                if buy == 1:

                    ans = max(prices[ind] + dp[0][ind+1] , 0 + dp[1][ind+1]) # sell or dont do any

                dp[buy][ind] = ans
            
        for row in dp:

            print(row)

        return dp[0][0]

