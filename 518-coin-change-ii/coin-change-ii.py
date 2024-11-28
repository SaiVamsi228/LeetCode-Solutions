class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        
        def getWaysCoins(n, amt):

            if amt == 0:

                return 1
            
            if n == 0:

                return 0
            
            if dp[n][amt] != -1:

                return dp[n][amt]

            if coins[n-1] <= amt :

                take = getWaysCoins(n, amt - coins[n-1])

                notTake = getWaysCoins(n-1, amt)

                dp[n][amt] = take + notTake
            
            else:

                dp[n][amt] =  getWaysCoins(n-1, amt)
            
            return dp[n][amt]
        
        n = len(coins)

        dp = [ [-1 for i in range(amount+1)] for j in range(n+1)]

        return getWaysCoins(n,amount)
        
