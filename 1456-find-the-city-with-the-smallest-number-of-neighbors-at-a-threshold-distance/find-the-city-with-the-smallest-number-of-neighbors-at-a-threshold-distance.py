class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dist = [ [float('inf') for i in range(n)] for j in range(n)]

        for i in range(n):

            for j in range(n):

                if i == j :

                    dist[i][j] = 0

        for u,v,wt in edges:

            dist[u][v] = wt

            dist[v][u] = wt
        
        for k in range(n):

            for u in range(n):

                for v in range(n):

                    if dist[u][k] != float('inf') and dist[k][v] != float('inf'):

                        dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
        
        city_threshold_cnt = [0 for i in range(n)]

        for i in range(n):

            cnt = 0

            for j in range(n):

                if i == j:

                    continue
                
                if dist[i][j] <= distanceThreshold:

                    cnt += 1
            
            city_threshold_cnt[i] = cnt

        mini, ans_city = float('inf'), -1

        for i in range(n):

            if city_threshold_cnt[i] < mini:

                mini = city_threshold_cnt[i]

                ans_city = i
        
            elif city_threshold_cnt[i] == mini:

                ans_city = i
        
        return ans_city