from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        n = numCourses

        def getAdj():

            adj = [ [] for i in range(n)]

            for a, b in prerequisites:

                adj[a].append(b)
            
            return adj

        adj = getAdj()

        def getTopoCnt():

            topoCnt = 0

            indegree = [0 for i in range(n)]

            for node in range(n):

                for neighbour in adj[node]:

                    indegree[neighbour] += 1

            q = deque()

            for i in range(n):

                if indegree[i] == 0:

                    q.append(i)
                
            while q :

                curNode = q.popleft()

                topoCnt += 1

                for neighbour in adj[curNode]:

                    indegree[neighbour] -= 1

                    if indegree[neighbour] == 0:

                        q.append(neighbour)
            
            return topoCnt 
        
        topoSortCnt = getTopoCnt()

        if topoSortCnt == n:

            return True
        
        return False
        
        