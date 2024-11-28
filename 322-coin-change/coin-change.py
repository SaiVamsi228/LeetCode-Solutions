class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def getMinCoins(n, amt):

            if amt == 0:

                return 0
            
            if n == 0:

                return float('inf')
            
            if dp[n][amt] != -1 :

                return dp[n][amt]

            if coins[n-1] <= amt :

                take = 1 + getMinCoins(n, amt - coins[n-1])

                notTake = getMinCoins(n-1, amt)

                dp[n][amt] = min(take , notTake)
            
            else:

                dp[n][amt] =  getMinCoins(n-1, amt)
            
            return dp[n][amt]
        
        n = len(coins)

        dp = [ [-1 for j in range(amount+1)] for i in range(n+1)]

        for i in range(n+1):

            for j in range(amount + 1):
                    
                if j == 0:

                    dp[i][j] = 0
                
                if i == 0 :

                    dp[i][j] = float('inf')
        
        for i in range(1,n +1):

            for j in range(1, amount + 1):

                if coins[i-1] <= j :

                    take = 1 + dp[i][j - coins[i-1]]

                    notTake = dp[i-1][j]

                    dp[i][j] = min(take, notTake)
                
                else:

                    notTake = dp[i-1][j]

                    dp[i][j] = notTake

        ans = dp[n][amount]
        
        if ans == float('inf'):

            return -1
        
        return ans