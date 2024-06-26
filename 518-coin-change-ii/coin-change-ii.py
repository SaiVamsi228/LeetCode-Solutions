class Solution:
    def memoChange(self, n, amt, coins, dp):

        if n==0 or amt == 0:

            if amt == 0:

                return 1

            if n == 0:

                return 0
        
        if dp[n][amt] != -1:

            return dp[n][amt]
        
        if coins[n-1] <= amt:

            dp[n][amt] = self.memoChange(n, amt - coins[n-1], coins, dp) + self.memoChange(n-1, amt, coins, dp) 
            
        else:

            dp[n][amt] = self.memoChange(n-1, amt, coins, dp)
        
        return dp[n][amt]

    def change(self, amount: int, coins: list[int]) -> int:

        n = len(coins)

        dp = [ [-1 for i in range(amount+1)] for j in range(n+1)]
        
        return self.memoChange(len(coins), amount, coins, dp)