class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [1 for i in range(n)]

        for curInd in range(n):

            for prevInd in range(curInd):

                if nums[curInd] > nums[prevInd]:

                    newLength = 1 + dp[prevInd]

                    dp[curInd] = max(dp[curInd], newLength)

        return max(dp)