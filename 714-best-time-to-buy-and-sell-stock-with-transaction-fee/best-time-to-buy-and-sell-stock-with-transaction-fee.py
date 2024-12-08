class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)

        def getMaxProfit(ind,buy):

            if ind == n:

                return 0
            
            if dp[buy][ind] != -1 :

                return dp[buy][ind]
            
            if buy == 0 :

                ans = max(-prices[ind] - fee + getMaxProfit(ind+1,1) , 0 + getMaxProfit(ind+1,0)) # buy or dont do any
            
            if buy == 1:

                ans = max(prices[ind] + getMaxProfit(ind+1,0) , 0 + getMaxProfit(ind+1,1)) # sell or dont do any

            dp[buy][ind] = ans

            return ans
        
        dp = [ [-1 for _ in range(n)] for j in range(2)]

        return getMaxProfit(0,0)

