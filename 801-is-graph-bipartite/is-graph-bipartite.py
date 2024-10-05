class Solution:
    def getIsBipartite(self,v, graph, visited,actColor):

        if v in visited:

            if visited[v] != actColor:
                            
                return False
            
            return True
        
        visited[v] = actColor
                
        isBipartite = True

        for neighbour in graph[v]:

            isBipartite = isBipartite and self.getIsBipartite(neighbour, graph, visited,actColor ^ 1)

        return isBipartite
        
                        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        visited = {}
        
        V = len(graph)
        
        for v in range(V):
            
            if v not in visited :
                
                if not self.getIsBipartite(v, graph, visited,0):
                    
                    return False
        
        return True
        
        
        