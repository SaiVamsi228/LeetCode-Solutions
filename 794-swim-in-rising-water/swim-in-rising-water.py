class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUpar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUpar(self.parent[node])  # Path compression
        return self.parent[node]

    def unionByRank(self, u, v):
        ulParU = self.findUpar(u)
        ulParV = self.findUpar(v)
        if ulParU == ulParV:
            return

        if self.rank[ulParU] < self.rank[ulParV]:
            self.parent[ulParU] = ulParV
        elif self.rank[ulParU] > self.rank[ulParV]:
            self.parent[ulParV] = ulParU
        else:
            self.parent[ulParV] = ulParU
            self.rank[ulParU] += 1

    def unionBySize(self, u, v):
        ulParU = self.findUpar(u)
        ulParV = self.findUpar(v)
        if ulParU == ulParV:
            return

        if self.size[ulParU] < self.size[ulParV]:
            self.parent[ulParU] = ulParV
            self.size[ulParV] += self.size[ulParU]
        else:
            self.parent[ulParV] = ulParU
            self.size[ulParU] += self.size[ulParV]


class Solution:
    def isValid(self, r, c, n):
        return 0 <= r < n and 0 <= c < n

    def swimInWater(self, grid):
        n = len(grid)
        ds = DisjointSet(n * n)

        # Store the position of each value in the grid as it is random position numbering
        position = [[] for _ in range(n * n)]
        for row in range(n):
            for col in range(n):
                position[grid[row][col]] = [row, col]

        # Directions for moving in the grid
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]

        # Process each cell in increasing order of time
        for time in range(n * n):
            row, col = position[time]

            # Check all four directions for possible paths
            for idx in range(4):
                nr, nc = row + dr[idx], col + dc[idx]

                if self.isValid(nr, nc, n) and grid[nr][nc] <= time:
                    ds.unionBySize(row * n + col, nr * n + nc)

            # Check if start and end are connected
            if ds.findUpar(0) == ds.findUpar(n * n - 1):
                return time

        return -1
