class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m , n = len(matrix), len(matrix[0])

        row_st = set()
        col_st = set()

        for row in range(m):

            for col in range(n):

                if matrix[row][col] == 0:

                    row_st.add(row)

                    col_st.add(col)
    

        for row in range(m):

            for col in range(n):

                if (row in row_st) or (col in col_st) :

                    matrix[row][col] = 0
        return matrix 