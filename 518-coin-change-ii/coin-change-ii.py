class Solution:

    def change(self, amt: int, coins: list[int]) -> int:

        n = len(coins)

        dp = [ [-1 for i in range(amt+1)] for j in range(n+1)]

        
        for i in range(n+1):
            
            for j in range(amt+1):
                    
                if i == 0:

                    dp[i][j] = 0
            
                if j == 0:

                    dp[i][j] = 1
                
        
        for i in range(1, n+1):

            for j in range(1,amt+1):

                if coins[i-1] <= j:

                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j] 
            
                else:

                    dp[i][j] = dp[i-1][j]
        
        return dp[n][amt]