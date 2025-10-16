class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        dr = [0,0,1,-1]

        dc = [1,-1,0,0]

        def isValid(r,c,m,n):

            return (0 <= r < m and 0 <= c < n)
        
        def changeColorToDes(r,c,color):

            if image[r][c] == color:

                return
            
            if image[r][c] == src_color:

                image[r][c] = color

                for i in range(4):

                    nr, nc = r + dr[i], c + dc[i]

                    if isValid(nr,nc,m,n):

                        changeColorToDes(nr,nc,color)
        
        m = len(image)

        n = len(image[0])
        
        src_color = image[sr][sc]

        changeColorToDes(sr,sc,color)

        return image


            
            