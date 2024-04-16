class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m , n = len(matrix), len(matrix[0])

        row_arr = [0]*m
        col_arr = [0]*n

        for row in range(m):

            for col in range(n):

                if matrix[row][col] == 0:

                    row_arr[row] = 1

                    col_arr[col] = 1
    

        for row in range(m):

            for col in range(n):

                if row_arr[row]==1 or col_arr[col] == 1 :

                    matrix[row][col] = 0
        return matrix 