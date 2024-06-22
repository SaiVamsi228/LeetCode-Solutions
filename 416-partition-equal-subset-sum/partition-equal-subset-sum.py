class Solution:
    
    def isSubsetSum (self, N, arr, sum):
        # code here 
        
        dp = [[-1 for _ in range(sum+1)] for _ in range(N+1)]
        
            
        for i in range(N + 1):
            
            for j in range(sum+1):
                
                if i==0:
                    
                    dp[i][j] = 0
                    
                if j == 0:
                    
                    dp[i][j] = 1 # IMP for 00 it should be Trur first dry run and write
                
            
        for i in range(1,N+1):
            
            for j in range(1,sum+1):
                
                if arr[i-1] <= j:
            
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]

                else:
            
                    dp[i][j] = dp[i-1][j]
            
        return dp[N][sum]

    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        Sum = sum(nums)

        if Sum % 2 == 1:

            return False

        halfSum = Sum // 2

        return self.isSubsetSum(n, nums, halfSum)
                


