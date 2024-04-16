class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m , n = len(matrix), len(matrix[0])

        first_row_zeroes = False

        first_col_zeroes = False

        for col in range(n):

            if matrix[0][col] == 0:

                first_row_zeroes = True

                break
        
        for row in range(m):

            if matrix[row][0] == 0:

                first_col_zeroes = True

                break
        
        for row in range(1,m):

            for col in range(1,n):

                if matrix[row][col] == 0:

                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1,m):

            for col in range(1,n):

                if matrix[0][col] == 0 or matrix[row][0] == 0:

                    matrix[row][col] = 0


        if first_row_zeroes :

            for col in range(n):

                matrix[0][col] = 0

        if first_col_zeroes:

            for row in range(m):

                matrix[row][0] = 0
        
        return matrix




