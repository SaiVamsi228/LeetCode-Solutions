class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        def getMaxProfit(ind,buy,k):

            if k == 0:

                return 0

            if ind == n:

                return 0
            
            if (ind,buy,k) in dp:

                return dp[(ind,buy,k)]
            
            if buy == 0:

                # can buy

                buy_now = -prices[ind] + getMaxProfit(ind+1,1,k)

                # dont buy

                dont_buy = getMaxProfit(ind+1,buy,k)
                
                dp[(ind,buy,k)] = max(buy_now,dont_buy)
            
            else:

                # can sell

                sell_now = prices[ind] + getMaxProfit(ind+1,0,k-1)

                dont_sell = getMaxProfit(ind+1,buy,k)

                dp[(ind,buy,k)] = max(sell_now, dont_sell)
            
            return dp[(ind,buy,k)]
            
        n = len(prices)

        dp = {}
        
        return getMaxProfit(0,0,k)




