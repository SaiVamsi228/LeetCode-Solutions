class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def getIsBp(node,prev):
            if color[node] != -1:
                if color[node] == prev:
                    return False
                else:
                    return True
            
            color[node] = prev ^ 1
            
            for neighbour in graph[node]:
                if getIsBp(neighbour,prev^1) == False:
                    return False
            
            return True

        n = len(graph)
        color = [-1 for i in range(n)]

        for node in range(n):
            if color[node] == -1:
                if getIsBp(node,0) == False:
                    return False

        return True


