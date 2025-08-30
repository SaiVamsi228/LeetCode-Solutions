class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        s1 = s

        s2 = t

        m = len(s1)

        n = len(s2)

        dp = [0 for i in range(n+1)] 

        dp[0] = 1

        for i in range(1,m+1):

            new_dp = [0 for k in range(n+1)]

            new_dp[0] = 1

            for j in range(1,n+1):

                if s1[i-1] == s2[j-1]:

                    take_cnt =  dp[j-1]

                    not_take_cnt = dp[j]

                    new_dp[j] = take_cnt + not_take_cnt
                
                else:

                    new_dp[j] = dp[j]

            dp = new_dp.copy()

        return dp[n]