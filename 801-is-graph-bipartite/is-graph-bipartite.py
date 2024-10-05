class Solution:
    def getIsBipartite(self,v, graph, visited):
        
        q = deque()
        
        q.append(v)
        
        color = 0
        
        visited[v] = color
        
        while q:
            
            n = len(q)
            
            for _ in range(n):
                
                curNode = q.popleft()
                
                color = visited[curNode]
                
                for neighbour in graph[curNode]:
                    
                    if neighbour in visited :
                        
                        if visited[neighbour] == color:
                            
                            return False
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        visited[neighbour] = color ^ 1
                        
                        q.append(neighbour)
        
        return True
        
                        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        visited = {}
        
        V = len(graph)
        
        for v in range(V):
            
            if v not in visited :
                
                if not self.getIsBipartite(v, graph, visited):
                    
                    return False
        
        return True
        
        
        