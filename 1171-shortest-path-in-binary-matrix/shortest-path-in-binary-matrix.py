from collections import deque

class Solution:
    def isValid(self, grid, row, col, n):
        if 0 <= row < n and 0 <= col < n and grid[row][col] == 0:
            return True
        return False

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Edge case: if the start or end is blocked, return -1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # Create deque
        dq = deque()

        # Distance array initialized with infinity
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        dist[0][0] = 1

        # Push the source with distance 1
        dq.append((0, 0, 1))  # (row, col, distance)

        # Directions for 8 possible moves (up, down, left, right, diagonals)
        dr = [0, 0, 1, -1, 1, -1, 1, -1]
        dc = [1, -1, 0, 0, 1, 1, -1, -1]

        # BFS using deque
        while dq:
            row, col, d = dq.popleft()

            # If we reach the destination, return the distance
            if row == n-1 and col == n-1:
                return d

            # Explore all 8 directions
            for k in range(8):
                nrow, ncol = row + dr[k], col + dc[k]

                if self.isValid(grid, nrow, ncol, n) and d + 1 < dist[nrow][ncol]:
                    dist[nrow][ncol] = d + 1
                    dq.append((nrow, ncol, d + 1))

        # If destination not reached, return -1
        return -1
