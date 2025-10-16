class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def getGraph(matrix):

            n = len(matrix)

            adj = [[] for i in range(n)]

            for i in range(n):

                for j in range(n):

                    if matrix[i][j] == 1:

                        adj[i].append(j)

                        adj[j].append(i)
            
            return adj
        
        adj = getGraph(isConnected)

        n = len(adj)

        def dfs(node):

            if visited[node]:

                return 
            
            visited[node] = True

            for neighbour in adj[node]:

                dfs(neighbour)
        
        cnt = 0
        
        visited = [False for i in range(n)]

        for node in range(n):

            if not visited[node]:

                dfs(node)

                cnt += 1
        
        return cnt
                    
