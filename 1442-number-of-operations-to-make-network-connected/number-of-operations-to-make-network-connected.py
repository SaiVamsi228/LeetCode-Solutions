class uf:

    def __init__(self,n) -> None:
        
        self.parent = [i for i in range(n)]

        self.rank  = [1 for i in range(n)]
    
    def findPar( self, v):

        if self.parent[v] == v:

            return v
        
        self.parent[v] = self.findPar(self.parent[v])

        return self.parent[v]
    
    def union(self, u, v):

        up_u = self.findPar(u)

        up_v = self.findPar(v)

        rank_upu = self.rank[up_u]

        rank_upv = self.rank[up_v]

        if rank_upu == rank_upv:

            self.parent[up_u] = up_v
        
        elif rank_upu > rank_upv:

            self.parent[up_v] = up_u

        elif rank_upu < rank_upv:

            self.parent[up_u] = up_

class Solution:

    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        
        network = uf(n)

        hp = connections.copy()

        heapify(hp)

        extraCablesAvailable = 0

        connected = 0

        visited = [0 for i in range(n)]

        while hp:

            src, dest = heappop(hp)

            if network.findPar(src) == network.findPar(dest):               
                extraCablesAvailable += 1

                continue

            network.union(src, dest)

            visited[src] = 1

            visited[dest] = 1

            connected += 1
        
        unconnectedComputer = n - (connected + 1)

        minCablesReq = unconnectedComputer 

        if minCablesReq > extraCablesAvailable:

            return -1

        return minCablesReq 
