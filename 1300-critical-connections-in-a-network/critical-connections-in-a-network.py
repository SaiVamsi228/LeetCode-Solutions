from typing import List

class Solution:

    def __init__(self):
        self.timer = 0

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def dfs(node, parent):
            visited[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1

            for neighbour in adj[node]:
                if neighbour == parent:
                    continue

                if not visited[neighbour]:
                    dfs(neighbour, node)
                    low[node] = min(low[node], low[neighbour])  # FIXED

                    if low[neighbour] > tin[node]:
                        bridges.append([node, neighbour])
                else:
                    low[node] = min(low[node], tin[neighbour])  # back edge

        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        tin = [0] * n
        low = [0] * n
        visited = [False] * n
        bridges = []

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return bridges
