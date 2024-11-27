class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        totSum = sum(nums)

        dp = [ [0 for i in range(totSum + 1)] for j in range(n+1)]

        dp[0][0] = 1

        # s1 + s2 = totSum
        # s1 - s2 = target
        newTotSum = totSum - target

        if newTotSum % 2 == 1 or abs(target) > totSum :

            return 0

        for i in range(1,n+1):

            for j in range(totSum + 1):

                if nums[i-1] <= j:

                    take = dp[i-1][j - nums[i-1]]

                    notTake = dp[i-1][j]

                    dp[i][j] = take + notTake
                
                else:

                    dp[i][j] = dp[i-1][j]
        
        
        
        searchSum = newTotSum // 2

        return dp[n][searchSum]