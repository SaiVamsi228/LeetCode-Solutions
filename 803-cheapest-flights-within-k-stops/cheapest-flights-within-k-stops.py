from heapq import heapify, heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        def get_graph(flights):

            adj = [[] for i in range(n)]

            for s,d,cst in flights:

                adj[s].append((d,cst))
            
            return adj

        adj = get_graph(flights)

        hp = []

        heapify(hp)

        # src, dest = > given

        cost_array = [[float('inf') for i in range(k+1)] for j in range(n)] # dist to be travelled to reach within k stops
        
        for stps in range(k+1):
            
            cost_array[src][stps] = 0

        pair = (src,0,-1) # (src city,cst incurred, stops taken)
        
        heappush(hp,pair)

        while hp:

            city, expenses, stops = heappop(hp)

            for neighbour_city, cost in adj[city]:

                new_stops = stops + 1

                new_cost = expenses + cost

                if new_stops <= k :

                    if new_cost < cost_array[neighbour_city][new_stops]:

                        cost_array[neighbour_city][new_stops] = new_cost

                        heappush(hp,(neighbour_city,new_cost,new_stops))

        mini_cost_within_k_stops = min(cost_array[dst])

        if mini_cost_within_k_stops == float('inf'):

            return -1
        
        return mini_cost_within_k_stops






