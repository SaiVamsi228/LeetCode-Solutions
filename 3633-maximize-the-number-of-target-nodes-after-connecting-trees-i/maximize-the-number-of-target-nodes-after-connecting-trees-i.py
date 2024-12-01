from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        n = len(edges1) + 1 
        
        m = len(edges2) + 1 

        def getAdjList(edges, n):
            
            adj = [ [] for i in range(n)]
            
            for u,v in edges:
                
                adj[u].append(v)
                
                adj[v].append(u)
            
            return adj

        def getNeighboursAtDistK(adj, n, k):
            
            dist = [ 0 for i in range(n)]

            q = deque()

            steps = 0

            parent = -1

            for src in range(n):

                q.append((src, steps, parent, src))

            while q :

                node, steps , parent , src = q.popleft()

                if steps <= k :

                    dist[src] += 1
                
                for neighbour in adj[node]:

                    if neighbour == parent :

                        continue

                    if steps + 1 <= k :

                        q.append((neighbour, steps + 1 , node, src))
            
            return dist
        
        adj1 = getAdjList(edges1, n)
        
        adj2 = getAdjList(edges2, m)

        dist_arr_1 = getNeighboursAtDistK(adj1,n,k )
        dist_arr_2 = getNeighboursAtDistK(adj2,m, k-1)

        mx = max(dist_arr_2)

        for i,a in enumerate(dist_arr_1):

            dist_arr_1[i] += mx

        return dist_arr_1