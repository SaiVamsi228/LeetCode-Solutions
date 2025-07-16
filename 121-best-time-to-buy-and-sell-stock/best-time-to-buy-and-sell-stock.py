class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]

        maxi = prices[0]

        n = len(prices)

        mx = 0

        for i in range(n):

            mini = min(mini,prices[i])

            mx = max(mx, prices[i] - mini)
        
        return mx