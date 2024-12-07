class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        aheadNotBuy, aheadBuy = -1, -1

        curNotBuy, curBuy = -1, -1

        aheadNotBuy = aheadBuy = 0
        
        for ind in reversed(range(n)): 

            curNotBuy = max(-prices[ind] + aheadBuy , 0 + aheadNotBuy) # buy or dont do any
            
            curBuy = max(prices[ind] + aheadNotBuy, 0 + aheadBuy) # sell or dont do any
            
            aheadNotBuy, aheadBuy = curNotBuy , curBuy

        return curNotBuy

