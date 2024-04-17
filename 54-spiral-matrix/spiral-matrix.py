class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        top = 0

        bottom = m - 1

        left = 0

        right = n - 1

        ans = []

        while top <= bottom and left <= right:

            for i in range(left,right+1):

                ans.append(matrix[top][i])
            
            top+=1

            if top > bottom:
                break

            for j in range(top,bottom+1):

                ans.append(matrix[j][right])
            
            right -=1

            if  left > right:

                break

            for k in range(right,left-1,-1):

                ans.append(matrix[bottom][k])
            
            bottom -=1

            if top > bottom :

                break

            for l in range(bottom,top-1,-1):

                ans.append(matrix[l][left])
            
            left+=1

            if left > right :

                break
        
        return ans