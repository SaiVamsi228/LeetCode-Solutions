class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def get_path_cnt(row,col):

            if row == m-1 and col == n-1 :

                return 1
            
            if row >= m or col >= n :

                return 0
            
            if dp[row][col] != -1:

                return dp[row][col]
            
            dp[row][col] = get_path_cnt(row+1,col) + get_path_cnt(row,col+1)

            return dp[row][col]

        dp = [ [-1 for i in range(n)] for j in range(m)]

        return get_path_cnt(0,0)