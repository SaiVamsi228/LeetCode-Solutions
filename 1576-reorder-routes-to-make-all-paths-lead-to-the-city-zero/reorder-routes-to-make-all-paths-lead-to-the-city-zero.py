class Solution:
    def getAdjList(self, graph, n):

        adj = [ [] for i in range(n) ]

        for u,v in graph:

            adj[u].append((v, 1))

            adj[v].append((u, -1))
        
        return adj

    def getMinReorientToReachHospital(self, city, adj, n, parent, minChange):

        for neighbour, direction in adj[city]:

            if neighbour == parent :

                continue

            if direction == 1:
                
                minChange[0] += 1
            
            self.getMinReorientToReachHospital(neighbour, adj, n, city, minChange)
        
        return minChange

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adj = self.getAdjList(connections,n)

        minChange = [0]
        
        self.getMinReorientToReachHospital(0, adj, n, -1, minChange)

        return minChange[0]