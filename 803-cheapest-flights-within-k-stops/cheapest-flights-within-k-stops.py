class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        def getGraph(edges,n):

            adj = [[] for i in range(n)]

            for u,v,w in edges:

                adj[u].append((v,w))
            
            return adj
        
        cost_chart = [[float('inf') for i in range(k+1)] for j in range(n)]

        for s in range(k+1):

            cost_chart[src][s] = 0
        
            
        adj = getGraph(flights,n)

        hp = []

        heapify(hp)

        cost, stops, city = 0,-1,src

        if city == dst:
            
            return cur_cost

        heappush(hp,(cost,stops,city))

        while hp:

            cur_cost,stops,city = heappop(hp)

            for neighbour, wt in adj[city]:

                new_cost, new_stops = cur_cost + wt, stops + 1

                if new_stops <= k and new_cost < cost_chart[neighbour][new_stops]:

                    cost_chart[neighbour][new_stops] = new_cost

                    heappush(hp,(new_cost,new_stops,neighbour))

        min_cost = min(cost_chart[dst])

        if min_cost == float('inf'):

            return -1
        
        return min_cost
