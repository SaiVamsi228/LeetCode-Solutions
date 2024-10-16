class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for i in range(n+1)]

        for s, d, t in times:

            adj[s].append([d,t])
        
        travelTime = [float('inf') for i in range(n+1)]

        hp = []

        heapify(hp)

        travelTime[k] = 0

        heappush(hp,(0,k))

        while hp:

            curTime, node = heappop(hp)

            for neighbour,time in adj[node]:

                newTime = curTime + time

                if newTime < travelTime[neighbour] :

                    travelTime[neighbour] = newTime

                    heappush(hp,(newTime, neighbour))
   
        travelTime[0] = 0

        mx = max(travelTime) 

        if mx == float('inf') :

            return -1
        
        return mx
                

