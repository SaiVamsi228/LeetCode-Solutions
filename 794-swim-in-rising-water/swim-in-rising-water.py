from heapq import heapify,heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        m = len(grid)

        n = len(grid[0])

        def isValid(r,c):

            return 0 <= r < m and 0 <= c < n
        
        hp = []

        heapify(hp)

        row,col = 0,0

        min_time = float('inf')

        heappush(hp,(0,row,col)) # cur_time, row , col 

        visited = set()

        dr = [0,0,1,-1]

        dc = [1,-1,0,0]

        time = grid[0][0]

        visited.add((0,0))

        while hp :

            cur_time,r,c = heappop(hp)

            time = max(time,cur_time)

            if r == m-1 and c == n-1:

                break

            for k in range(4):

                new_r, new_c = r + dr[k], c + dc[k]

                if isValid(new_r,new_c) and (new_r,new_c) not in visited:

                    new_time = grid[new_r][new_c]

                    new_mx = max(cur_time,new_time)

                    visited.add((new_r,new_c))

                    heappush(hp,(new_mx,new_r,new_c))
        

        return time
            



                    
                    