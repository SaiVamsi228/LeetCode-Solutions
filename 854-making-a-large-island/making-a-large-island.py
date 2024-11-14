from typing import List
class unionFind:
    def __init__(self, n):

        self.parent = [ i for i in range(n)]

        self.size = [ 1 for i in range(n)]

        self.rank = [0 for i in range(n)]

    def findUPar(self, v):

        if self.parent[v] == v:

            return v

        self.parent[v] = self.findUPar(self.parent[v])

        return self.parent[v] 

    def unionByRank(self, u, v):

        up_u = self.findUPar(u)

        up_v = self.findUPar(v)

        rank_up_u = self.parent[up_u]

        rank_up_v = self.parent[up_v]

        if rank_up_u < rank_up_v:

            self.parent[up_u] = up_v
        
        elif rank_up_u > rank_up_v:

            self.parent[up_v] = up_u
        
        else:

            self.parent[up_u] = up_v

            self.rank[up_u] += 1
    
    def unionBySize(self, u, v):

        up_u = self.findUPar(u)

        up_v = self.findUPar(v)

        size_up_u = self.size[up_u]

        size_up_v = self.size[up_v]

        if size_up_u < size_up_v :

            self.parent[up_u] = up_v

            self.size[up_v] += self.size[up_u]

        elif size_up_u > size_up_v :

            self.parent[up_v] = up_u

            self.size[up_u] += self.size[up_v]
        
        else:
            
            self.parent[up_v] = up_u

            self.size[up_u] += self.size[up_v]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)

        n = len(grid[0])

        def isValid(row, col):

            return 0 <= row < m and 0 <= col < n

        ds = unionFind(m*n)

        dr = [0 , 0 , 1 , -1]

        dc = [1 , -1 , 0 , 0 ]

        for row in range(m):

            for col in range(n):

                nodeNo = row * n + col 

                if grid[row][col] == 1:

                    for k in range(4):

                        adjR, adjC = row + dr[k] , col + dc[k]

                        if isValid(adjR, adjC) and grid[adjR][adjC] == 1: 

                            adjNodeNo = adjR * n + adjC

                            up_cur = ds.findUPar(nodeNo)

                            up_adj = ds.findUPar(adjNodeNo)

                            if up_cur != up_adj:

                                ds.unionBySize(nodeNo, adjNodeNo)
        
        largestIslandFound = max(ds.size)

        for row in range(m):

            for col in range(n):

                if grid[row][col] == 0:

                    curIslandSize = 1

                    # go four directionally and check if it is land over there , if it is a land add the size of that comp
                    # and store its parent bcz we may encounter other cell of the current parent comp as our neighbour 
                    # by storing we can verify if it is the same comp or not if its the same comp ignore it bcs we have already
                    # taken its size else just add up

                    recent_parents = set()

                    for k in range(4):

                        adjR, adjC = row + dr[k] , col + dc[k]

                        if isValid(adjR, adjC) and grid[adjR][adjC] == 1: 

                            adjNodeNo = adjR * n + adjC



                            up_adjNode = ds.findUPar(adjNodeNo)

                            if up_adjNode  in recent_parents:

                                continue

                            adjCompSize = ds.size[up_adjNode]

                            curIslandSize += adjCompSize

                            recent_parents.add(up_adjNode)

                    largestIslandFound = max(largestIslandFound, curIslandSize)
        
        return largestIslandFound
                    
                        



            

                        
                
        
                        

                        