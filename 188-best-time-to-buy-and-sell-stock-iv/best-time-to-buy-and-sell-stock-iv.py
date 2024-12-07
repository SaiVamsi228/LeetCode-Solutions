class Solution:
    def maxProfit(self,k, prices: list[int]) -> int:
        
        n = len(prices)

        ahead = [[0 for buy in range(2)] for trans in range(k+1+1)]

        cur = [[0 for buy in range(2)] for trans in range(k+1+1)]

        for ind in reversed(range(n)):

            for trans in reversed(range(k+1)):

                for buy in range(2):

                    if buy == 0: # buy or skip
                    
                        profit = max(-prices[ind] + ahead[trans+1][1] , 0 + ahead[trans][0])
                    
                    elif buy == 1: # sell or skip

                        profit = max( prices[ind] + ahead[trans][0] , 0 + ahead[trans][1])

                    
                    cur[trans][buy] = profit
            
            ahead = cur.copy()


        return ahead[0][0]

                

