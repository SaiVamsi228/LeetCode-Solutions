from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def getCntSubsetSum(n,target):

            if n == 0:

                if target == 0:

                    return 1

                return 0
            
            if (n,target) in dp:

                return dp[(n,target)]
            
            add_cnt = getCntSubsetSum(n-1,target-nums[n-1])

            sub_cnt = getCntSubsetSum(n-1,target+nums[n-1])

            dp[(n,target)] =  add_cnt + sub_cnt

            return dp[(n,target)]
        
        n = len(nums)

        dp = {}

        return getCntSubsetSum(n,target) 