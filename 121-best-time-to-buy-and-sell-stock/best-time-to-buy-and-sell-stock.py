class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        mini_arr = [prices[0] for i in range(n)]

        maxi_arr = [prices[n-1] for j in range(n)]

        for i in range(1,n):

            mini_arr[i]= min(prices[i],mini_arr[i-1])

        
        for j in reversed(range(n-1)):

            maxi_arr[j] = max(prices[j],maxi_arr[j+1])

        maxi_diff = 0

        for ind in range(n):

            diff = maxi_arr[ind] - mini_arr[ind]

            maxi_diff = max(maxi_diff,diff)

        return maxi_diff
