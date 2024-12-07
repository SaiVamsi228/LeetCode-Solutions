class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        ahead = [ -1 for j in range(2)]

        cur = [-1 for i in range(2)]

        ahead[0] = ahead[1] = 0
        
        for ind in reversed(range(n)): 

            cur[0] = max(-prices[ind] + ahead[1] , 0 + ahead[0]) # buy or dont do any
            
            cur[1] = max(prices[ind] + ahead[0] , 0 + ahead[1]) # sell or dont do any
            
            ahead[0], ahead[1] = cur[0] , cur[1]


        return cur[0]

