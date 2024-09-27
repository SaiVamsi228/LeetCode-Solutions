class Solution:
    def getList(self,mat,n):

        graph = [[] for i in range(n+1)]

        for i in range(n):

            for j in range(n):

                if i==j or mat[i][j] == 0:

                    continue
                
                else:

                    graph[i+1].append(j+1)
        
        return graph
    
    def dfs(self,v,adj,visited):

        for neighbour in adj[v]:
            
            if neighbour not in visited:

                visited.add(neighbour)

                self.dfs(neighbour, adj, visited)
        return

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)

        adj = self.getList(isConnected,n)

        cnt = 0

        visited = set()

        for i in range(1,n+1):

            if i not in visited:

                visited.add(i)

                self.dfs(i,adj,visited)

                cnt += 1
        
        return cnt