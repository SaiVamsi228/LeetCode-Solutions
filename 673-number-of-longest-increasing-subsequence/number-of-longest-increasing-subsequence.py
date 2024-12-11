class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [1 for i in range(n)]

        cnt = [1 for i in range(n)]

        maxi = 1


        for ind in range(n):

            curMaxi = dp[ind]

            for prev_ind in range(ind):

                if nums[ind] > nums[prev_ind]:

                    if dp[prev_ind] + 1 > dp[ind]:

                        dp[ind] = dp[prev_ind] + 1

                    if dp[prev_ind] + 1 == curMaxi :

                        cnt[ind] += cnt[prev_ind]
                    
                    elif dp[prev_ind] + 1 > curMaxi :

                        cnt[ind] = cnt[prev_ind]

                        curMaxi = dp[ind]

        maxi = max(dp)

        ans = 0

        for i in range(n):

            if dp[i] == maxi:

                ans += cnt[i]

        return ans