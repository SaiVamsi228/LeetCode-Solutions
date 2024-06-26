class Solution:
    def coinChange(self, coins: list[int], amt: int) -> int:
        
        n = len(coins)

        dp = [ [-1 for i in range(amt + 1)] for j in range(n+1)]
        
        for j in range(amt + 1): # making first row as 2**31 including 0 0 

            dp[0][j] = 2**31

        for i in range(1,n+1): # making first col as 0 excluding 0 0

            dp[i][0] = 0               

        for i in range(1, n+1):

            for j in range(1, amt + 1):
                
                if coins[i-1] <= j:

                    dp[i][j] = min( 1 + dp[i][j - coins[i-1]] , dp[i-1][j] )
        
                else:

                    dp[i][j] = dp[i-1][j]
        
        ans = dp[n][amt]

        return ans if ans != 2**31 else -1