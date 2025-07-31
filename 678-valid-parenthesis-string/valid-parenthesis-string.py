class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]

        dp[0] = True  # base case

        for i in range(n - 1, -1, -1):
            cur_dp = [False for i in range(n+1)]
            for bal in range(n):
                if s[i] == '(':
                    if bal + 1 <= n:
                        cur_dp[bal] = dp[bal + 1]
                elif s[i] == ')':
                    if bal - 1 >= 0:
                        cur_dp[bal] = dp[bal - 1]
                elif s[i] == '*':
                    cur_dp[bal] = dp[bal]
                    if bal + 1 <= n:
                        cur_dp[bal] |= dp[bal + 1]
                    if bal - 1 >= 0:
                        cur_dp[bal] |= dp[bal - 1]
            
            dp = cur_dp.copy()


        return dp[0]
