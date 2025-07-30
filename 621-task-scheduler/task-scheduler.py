from collections import deque, Counter
from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq_hm = Counter(tasks)

        hp = []

        heapify(hp)

        for ele,freq in freq_hm.items():

            heappush(hp,-1*freq)
        
        q = deque()

        time = 0

        while hp or q:

            if hp:
                
                freq = heappop(hp)

                freq = -1 * freq

                freq -= 1

                if freq > 0:
                
                    q.append((freq,time+n+1))

            time += 1

            while q and q[0][1] == time:

                freq, nxt = q.popleft()

                heappush(hp,-freq)
        

        while q :

            freq, nxt = q[0]

            if time >= nxt:
                
                freq -= 1

            if freq > 0:
                
                q.append((freq,time+n+1))

            time += 1

        return time

        



