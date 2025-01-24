class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)

        n = len(matrix[0])

        is_first_col_zero = False
        is_first_row_zero = False
        
        # checking if first col has 0

        for i in range(m):

            if matrix[i][0] == 0:

                is_first_col_zero = True

                break
        
        # checking if first row has 0

        for j in range(n):

            if matrix[0][j] == 0 :

                is_first_row_zero = True

                break

        for i in range(1,m):

            for j in range(1,n):

                if matrix[i][j] == 0:

                    matrix[0][j] = 0

                    matrix[i][0] = 0
            
        
        for i in range(1,m):

            for j in range(1,n):

                if matrix[i][0] == 0 or matrix[0][j] == 0:

                    matrix[i][j] = 0

        # if first col is zero

        if is_first_col_zero == True :
            
            for i in range(m):

                matrix[i][0] = 0
        
        # if first row is zero

        if is_first_row_zero == True :
            
            for j in range(n):            

                matrix[0][j] = 0

        return matrix
                
