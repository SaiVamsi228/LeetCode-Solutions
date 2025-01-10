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

            self.parent[up_u] = up_v

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        connections = uf(n+1)

        for u,v in edges:

            up_u = connections.findPar(u)

            up_v = connections.findPar(v)

            if up_u == up_v :

                return [u,v]
            
            else:

                connections.union(u,v)
        
        return []


