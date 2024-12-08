class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        ahead = [ [ 0 for buy in range(2)] for coolTime in range(2)]

        cur_day = [ [ -1 for buy in range(2)] for coolTime in range(2)]
        
        for day in reversed(range(n)):

            for buy in reversed(range(2)):

                for coolTime in reversed(range(2)) :

                    if buy == 0: # buy or leave
                
                        # before buying check cooling time

                        if coolTime == 0:

                            profit = max( -prices[day] + ahead[0][1] , 0 + ahead[0][0])
                        
                        else:

                            profit = 0 + ahead[coolTime - 1][0]

                    if buy == 1: #sell or leave
                        
                        profit = max(prices[day] + ahead[1][0] , 0 + ahead[0][1])

                    cur_day[coolTime][buy] = profit
            
            ahead = cur_day[:]

        return ahead[0][0]
            
