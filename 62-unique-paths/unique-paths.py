class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cur_row = [-1 for i in range(n)]

        cur_row[n-1] = 1

        for row in reversed(range(m)):

            for col in reversed(range(n)):

                if row == m-1 and col == n-1 :

                    continue
                
                if row + 1 < m :

                    bottom_ways = next_row[col]
                
                else:

                    bottom_ways = 0
                
                if col + 1 < n:

                    right_ways = cur_row[col+1]
                
                else:

                    right_ways = 0
                
                cur_row[col] = bottom_ways + right_ways
            
            next_row = cur_row.copy()

            cur_row = [-1 for i in range(n)]


        return next_row[0]