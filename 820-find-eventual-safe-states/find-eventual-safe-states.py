from collections import deque
class Solution:
    def getTopo(self,graph,n):

        indegree = [ 0 for i in range(n)]

        q = deque()

        for v in range(n):

            for neighbour in graph[v]:

                indegree[neighbour] += 1
        
        for i,inDeg in enumerate(indegree):

            if inDeg == 0:

                q.append(i)

        topo = []
        
        while q :

            curNode = q.popleft()

            topo.append(curNode)

            for neighbour in graph[curNode]:

                indegree[neighbour] -= 1
            
                if indegree[neighbour] == 0:

                    q.append(neighbour)
            
        topo.sort()
        
        return topo         
        
    def reverseEdges(self,graph):

        n = len(graph)

        ans = [[] for i in range(n)]

        for u in range(n):

            for v in graph[u]:

                ans[v].append(u)
        
        return ans



    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        stack = []

        n = len(graph)

        reversedGraph = self.reverseEdges(graph)

        return self.getTopo(reversedGraph,n)
        
         