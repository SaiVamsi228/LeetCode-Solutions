class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # node -> 0 or 1

        def bfs(start: int) -> bool:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Start with color 0

            while queue:
                node = queue.popleft()
                curr_color = color[node]

                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[neighbor] == curr_color:
                            return False  # Same color on both sides
                    else:
                        color[neighbor] = curr_color ^ 1  # Assign opposite color
                        queue.append(neighbor)

            return True

        for node in range(len(graph)):
            if node not in color:
                if not bfs(node):
                    return False

        return True
