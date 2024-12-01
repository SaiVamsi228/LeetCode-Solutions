from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        n = len(edges1) + 1 
        
        m = len(edges2) + 1 
        
        def getAdjList(edges):
            
            adj = [ [] for i in range(len(edges)+1)]
            
            for u,v in edges:
                
                adj[u].append(v)
                
                adj[v].append(u)
            
            return adj
        
        adj1 = getAdjList(edges1)
        
        adj2 = getAdjList(edges2)



        steps = 0

        dist_arr_2 = [0 for src in range(m)]

        for src in range(m):

            q = deque()

            q.append((src,0, -1))
            
            while q :

                node, steps, parent = q.popleft()

                if steps <= k - 1 :

                    dist_arr_2[src] += 1

                for neighbour in adj2[node] :

                    if neighbour == parent:

                        continue

                    if steps + 1 <= k - 1:

                        q.append((neighbour, steps + 1, node))

        dist_arr_1 = [0 for i in range(n)]

        for src in range(n):

            q = deque()

            q.append((src,0, -1))
            
            while q :

                node, steps, parent = q.popleft()

                if steps <= k :

                    dist_arr_1[src] += 1

                for neighbour in adj1[node] :

                    if neighbour == parent :

                        continue

                    if steps + 1 <= k :
                        
                        q.append((neighbour, steps + 1, node))
        
        ans = dist_arr_1

        mx = max(dist_arr_2)
        
        # print(dist_arr_1,mx)

        for i,a in enumerate(ans):

            ans[i] += mx

        return ans