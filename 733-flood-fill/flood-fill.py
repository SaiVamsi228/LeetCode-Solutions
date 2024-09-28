class Solution:
    def isValid(self,row,col,m,n):

        if 0 <= row < m and 0 <= col < n:

            return True
        
        return False
    
    def dfs(self,row,col,m,n,image,color,srcCol):

        drow = [1,-1,0,0]
        dcol = [0,0,1,-1]

        for i in range(4):

            nRow , nCol = row + drow[i] , col + dcol[i]

            if self.isValid(nRow,nCol,m,n) and image[nRow][nCol] == srcCol and image[nRow][nCol] != color:

                image[nRow][nCol] = color

                self.dfs(nRow,nCol,m,n,image,color,srcCol)
        
        return 

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row,col = sr,sc

        m,n = len(image), len(image[0])

        srcCol = image[sr][sc]

        image[sr][sc] = color

        self.dfs(row,col,m,n,image,color,srcCol)

        return image