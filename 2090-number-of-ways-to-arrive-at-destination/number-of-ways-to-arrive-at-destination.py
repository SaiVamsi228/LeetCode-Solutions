class Solution:
    def getAdjList(self,roads,n):

        adj = [[] for i in range(n)]

        for src, dest, time in roads:

            adj[src].append((dest,time))

            adj[dest].append((src, time))
        
        return adj
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        
        adj  = self.getAdjList(roads, n)

        time = [ float('inf') for i in range(n)]

        src = 0

        time[src] = 0

        ways = [0 for i in range(n)]

        ways[0] = 1

        parent = -1

        hp = []

        heapify(hp)

        heappush(hp, (time[src], src))


        while hp:

            curTime, node = heappop(hp)

            for neighbour,travel_time in adj[node]:
                
                newTime = curTime + travel_time

                if newTime < time[neighbour] :

                    time[neighbour] = newTime

                    ways[neighbour] = ways[node]

                    heappush(hp, (newTime, neighbour))
                
                elif newTime == time[neighbour]:

                    ways[neighbour] += ways[node]
                
                # if neighbour == n-1:

                #     print(node, ways)
                
        MOD = 10**9 + 7

        return ways[n-1] % MOD



