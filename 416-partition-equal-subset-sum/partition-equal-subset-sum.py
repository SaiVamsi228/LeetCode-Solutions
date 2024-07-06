class Solution:
    def hasSubsetSum(self, nums, Sum, n):

        dp = [[ False for i in range(Sum+1)] for j in range(n+1)]

        # Making all the ele of first row as False

        for i in range(Sum+1):

            dp[0][i] = False

        # Making all the ele of first col as True

        for j in range(n+1):

            dp[j][0] = True
        
        for i in range(1,n+1):

            for j in range(1,Sum+1):

                if nums[i-1] <= j:

                    dp[i][j] = dp[i-1][j - nums[i-1]] + dp[i-1][j]
                
                else:

                    dp[i][j] = dp[i-1][j]
        
        return dp[n][Sum]

        

    def canPartition(self, nums: List[int]) -> bool:
        
        Sum = sum(nums)

        # if my sum is odd i cant divide

        if Sum % 2 == 1:

            return False
        
        halfSum = Sum // 2

        n = len(nums)

        return self.hasSubsetSum(nums, halfSum, n)