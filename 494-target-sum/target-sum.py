class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def getCntSubsetSum(n,target):

            if n == 0:

                if target == 0:

                    return 1

                return 0
            
            if (n,target) in dp:

                return dp[(n,target)]
            
            take_cnt = getCntSubsetSum(n-1,target-nums[n-1])

            not_take_cnt = getCntSubsetSum(n-1,target)

            dp[(n,target)] =  take_cnt + not_take_cnt

            return dp[(n,target)]
        
        n = len(nums)

        tot_sum = sum(nums)

        if (tot_sum + target)%2 != 0 :

            return 0
        
        if target > tot_sum :

            return 0

        target_sum = (tot_sum + target)//2

        dp = {}

        return getCntSubsetSum(n,target_sum) 