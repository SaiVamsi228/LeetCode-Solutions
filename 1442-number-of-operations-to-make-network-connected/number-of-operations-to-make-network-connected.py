class unionFind:

    def __init__(self,n):

        self.parent = [i for i in range(n)]

        self.rank = [1 for i in range(n)]
    
    def findUParent(self,node):

        if self.parent[node] == node:

            return node
        
        self.parent[node] = self.findUParent(self.parent[node])

        return self.parent[node]
    
    def unionByRank(self,u,v):

        up_u = self.findUParent(u)
        up_v = self.findUParent(v)
        rank_up_u = self.rank[up_u]
        rank_up_v = self.rank[up_v]

        if rank_up_u > rank_up_v:

            self.parent[up_v] = up_u
        
        elif rank_up_v > rank_up_u:

            self.parent[up_u] = up_v
        
        else:

            self.parent[up_u] = up_v

            self.rank[up_v] += 1    

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        uf = unionFind(n)

        mn = 0

        connected = 0

        for u,v in connections:

            up_u = uf.findUParent(u)
            up_v = uf.findUParent(v)

            if up_u == up_v:

                continue
            
            connected += 1

            uf.unionByRank(u,v)
        
        total = n 

        unconnected = (total - 1) - connected

        extra_cables = len(connections) -  (total - 1)

        if extra_cables >= 0 :

            return unconnected
        
        return -1




        