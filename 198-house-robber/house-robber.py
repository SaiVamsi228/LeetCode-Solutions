class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def getMaxMoney(n):

            if n == 0:

                return 0
            
            if n == 1 :

                return nums[0]
            
            if n == 2:

                return max(nums[0],nums[1])
            
            if dp[n] != -1 :

                return dp[n]

            rob = nums[n-1] + getMaxMoney(n-2)

            dontRob = getMaxMoney(n-1)

            dp[n] = max(rob, dontRob)

            return dp[n]

        n = len(nums)

        dp = [-1 for i in range(n+1)]

        return getMaxMoney(n)             