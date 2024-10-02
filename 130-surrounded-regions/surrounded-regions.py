class Solution:
    def isValid(self, r,c,m,n,mat,visited):

        if 0 <= r < m and 0 <= c < n and not visited[r][c] and mat[r][c] == "O":

            return True
        
        return False
    def markVisited(self,r,c,m,n,mat,visited):

        visited[r][c] = 1

        dr, dc = [0,0,1,-1], [1,-1,0,0]

        for i in range(4):

            nr , nc = r + dr[i], c + dc[i]

            if self.isValid(nr,nc,m,n,mat,visited):

                self.markVisited(nr,nc,m,n,mat,visited)
        
        return 

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)

        n = len(board[0])

        visited = [ [0 for i in range(n)] for j in range(m)]

        for i in range(m):

            for j in range(n):

                if (i == 0 or i == m-1 or j == 0 or j == n-1 )and board[i][j] == "O":

                    self.markVisited(i,j,m,n,board,visited)

        for i in range(m):

            for j in range(n):

                if not visited[i][j] and board[i][j] == "O":

                    board[i][j] = "X"

                    visited[i][j] = 1
        
        return board

                



        