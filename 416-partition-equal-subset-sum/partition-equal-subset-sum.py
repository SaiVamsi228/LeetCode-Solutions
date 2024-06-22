class Solution:
    
    def memoIsSubsetSum(self,N,arr,sum,dp):
        
        if N==0 or sum == 0:
            
            if sum==0: return 1
            
            if N==0: return 0
            
        if dp[N][sum] != -1:
            
            return dp[N][sum]
            
        
        if arr[N-1] <= sum:
            
            dp[N][sum] = self.memoIsSubsetSum(N-1,arr,sum-arr[N-1],dp) or self.memoIsSubsetSum(N-1,arr,sum,dp)

        else:
            
            dp[N][sum] = self.memoIsSubsetSum(N-1,arr,sum,dp)
            
        return dp[N][sum]

    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        Sum = sum(nums)

        if Sum % 2 == 1:

            return False

        halfSum = Sum // 2

        dp = [[-1 for i in range(halfSum+1)] for j in range(n+1)]
        
        return self.memoIsSubsetSum(n, nums, halfSum,dp)
                


