class Solution:
    def climbStairs(self, n: int) -> int:
        
        def solve(n):

            if n == 1 :

                return 1
            
            if n == 2:

                return 2
            
            if dp[n] != - 1:

                return dp[n]

            one_step_ways = solve(n-1) 
            
            two_step_ways = solve(n-2)

            dp[n] = one_step_ways + two_step_ways

            return dp[n]
        
        dp = [-1 for i in range(n+1)]

        return solve(n)
        
