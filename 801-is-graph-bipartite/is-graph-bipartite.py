class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = {} # node => color

        def dfs(node,prev_color):

            if node in color: # if the node is already colored check it

                if color[node] == prev_color:

                    return False
                
                else:

                    return True
            
            color[node] = prev_color ^ 1
            
            for neighbour in graph[node]:

                if dfs(neighbour,prev_color^1) == False:

                    return False
            
            return True

        n = len(graph)
        
        for node in range(n):

            if node not in color and dfs(node,-1) == False:

                return False
        
        return True
                

