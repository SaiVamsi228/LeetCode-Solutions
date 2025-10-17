from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = deque()

        m = len(mat)

        n = len(mat[0])

        for i in range(m):

            for j in range(n):

                if mat[i][j] == 0:

                    q.append((i,j))
        
        dist = [[ float('inf') for i in range(n)] for j in range(m)]

        def isValid(r,c,m,n):

            return (0<=r<m and 0<=c<n)
        
        dr = [0,0,1,-1]

        dc = [1,-1,0,0]

        dis = 0

        while q:

            t = len(q)

            dis += 1

            for _ in range(t):

                r,c = q.popleft()

                for i in range(4):

                    nr,nc = r + dr[i], c + dc[i]

                    if isValid(nr,nc,m,n):

                        if mat[nr][nc] == 1:

                            if dis < dist[nr][nc] :

                                dist[nr][nc] = dis

                                q.append((nr,nc))
        
        for i in range(m):

            for j in range(n):

                if dist[i][j] == float('inf'):

                    dist[i][j] = 0

        return dist
                
                            


