class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        dp[n][0] = True  # base case

        for i in range(n - 1, -1, -1):
            for bal in range(n):
                if s[i] == '(':
                    if bal + 1 <= n:
                        dp[i][bal] = dp[i + 1][bal + 1]
                elif s[i] == ')':
                    if bal - 1 >= 0:
                        dp[i][bal] = dp[i + 1][bal - 1]
                elif s[i] == '*':
                    dp[i][bal] = dp[i + 1][bal]
                    if bal + 1 <= n:
                        dp[i][bal] |= dp[i + 1][bal + 1]
                    if bal - 1 >= 0:
                        dp[i][bal] |= dp[i + 1][bal - 1]

        return dp[0][0]
