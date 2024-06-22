class Solution:
    def recursiveCanPartition(self,nums,n,Sum,halfSum,dp):

        if n == 0 or Sum == halfSum:

            if Sum == halfSum:

                return True
            
            if n == 0:

                return False

        if dp[n][Sum]!=-1:

            return dp[n][Sum]

        if nums[n-1] <= halfSum:

            dp[n][Sum] = self.recursiveCanPartition(nums,n-1,Sum-nums[n-1],halfSum,dp) or self.recursiveCanPartition(nums,n-1,Sum,halfSum,dp)
        
        else:

            dp[n][Sum] = self.recursiveCanPartition(nums,n-1,Sum,halfSum,dp)
        
        return dp[n][Sum]

    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        Sum = sum(nums)

        if Sum % 2 == 1:

            return False

        halfSum = Sum // 2

        dp = [ [-1 for i in range(Sum + 1)] for j in range(n+1)]
        
        return self.recursiveCanPartition(nums,n-1,Sum,halfSum,dp)