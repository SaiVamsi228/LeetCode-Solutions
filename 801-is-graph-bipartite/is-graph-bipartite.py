class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)

        visited_color = [0 for i in range(n)]

        def getIsBipartite(node):

            q = deque()

            parent = -1

            q.append((node,parent))

            while q :

                node,par = q.popleft()

                color = visited_color[node]

                for neighbour in graph[node]:

                    if neighbour == par:

                        continue
                    
                    if visited_color[neighbour]:

                        n_color = visited_color[neighbour]

                        if color == n_color:

                            return False
                    
                    else:

                        n_color = 1 if color == 2 else 2

                        visited_color[neighbour] = n_color

                        q.append((neighbour,node))
            
            return True


        

        for node in range(n):

            if not visited_color[node]:

                if not getIsBipartite(node):

                    return False
        
        return True