class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(node,prev_color):

            if node in color:

                if color[node] == prev_color:

                    return False
                
                else:

                    return True
            
            color[node] = 1 if prev_color == 2 else 2

            for neighbour in graph[node]:

                if dfs(neighbour,color[node]) == False:

                    return False
            
            return True
        
        n = len(graph)

        for node in range(n):

            if node not in color:

                if dfs(node,-1) == False:

                    return False
        return True
        

            

            


