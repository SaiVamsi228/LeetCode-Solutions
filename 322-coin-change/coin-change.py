class Solution:

    def memoCoinChange(self, n, coins, amt, dp):

        if amt == 0 or n==0:

            if amt == 0:
                
                return 0
        
            if n == 0:

                return 2**31
        
        if dp[n][amt] != -1:

            return dp[n][amt]

        if coins[n-1] <= amt:

            dp[n][amt] = min( 1 + self.memoCoinChange(n, coins, amt - coins[n-1], dp) , self.memoCoinChange(n-1, coins, amt, dp))
        
        else:

            dp[n][amt] = self.memoCoinChange(n-1, coins, amt, dp)
        
        return dp[n][amt]



    def coinChange(self, coins: list[int], amount: int) -> int:
        
        n = len(coins)

        dp = [ [-1 for i in range(amount + 1)] for j in range(n+1)]

        ans = self.memoCoinChange(n,coins,amount, dp)
        
        return ans if ans != 2**31 else -1
