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

        ans = getMinCoins(n, amount)

        if ans == float('inf'):

            return -1
        
        return ans