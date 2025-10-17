class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        
        def isValid(r,c,m,n):

            return (0 <= r < m and 0 <= c < n)

        def dfs(r,c):
            
            node = board[r][c]

            if node == 0 :

                return
            
            board[r][c] = 0

            for i in range(4):

                nr, nc = r + dr[i], c + dc[i]

                if isValid(nr,nc,m,n):

                    dfs(nr,nc)
        
        dr = [0,0,1,-1]

        dc = [1,-1,0,0]

        q = deque()

        m = len(board)

        n = len(board[0])

        for row in range(m):

            for col in range(n):

                if row == 0 or row == m-1 or col == 0 or col == n-1:

                    node = board[row][col]

                    if node == 1:

                        q.append((row,col))
        
        while q:

            r,c = q.popleft()

            dfs(r,c)
        
        cnt = 0

        for i in range(m):

            for j in range(n):

                if board[i][j] == 1:

                    cnt += 1
        
        return cnt


        