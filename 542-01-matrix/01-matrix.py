class Solution:
    def isValid(self, r, c, m , n):

        if  0 <= r < m and 0 <= c < n :

            return True
        
        return False
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = []

        m = len(mat)

        n = len(mat[0])

        dist = [ [2**31 + 1 for j in range(n)] for i in range(m)]

        for i in range(m):

            for j in range(n):

                if mat[i][j] == 0:

                    q.append((i,j))

                    dist[i][j] = 0

        d = 1

        dr = [0,0,1,-1]

        dc = [1,-1,0,0]
        
        while q :

            n_ = len(q)

            for _ in range(n_):

                r,c = q.pop(0)

                for i in range(4):

                    nr, nc = r + dr[i] , c + dc[i]

                    if self.isValid(nr,nc,m,n):

                        if mat[nr][nc] == 1 and  d < dist[nr][nc]:

                            dist[nr][nc] = d

                            q.append((nr,nc))
                
            
            d += 1

        mat = dist

        return mat