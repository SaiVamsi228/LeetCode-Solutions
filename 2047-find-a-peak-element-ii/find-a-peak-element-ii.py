class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        peak_value = -1
        for i in range(rows):
            for j in range(cols):
                up = mat[i-1][j] if i > 0 else -1
                down = mat[i+1][j] if i < rows-1 else -1
                left = mat[i][j-1] if j > 0 else -1
                right = mat[i][j+1] if j < cols-1 else -1
                if mat[i][j] > max(up, down, left, right):
                    peak_value = mat[i][j]
                    break
            if peak_value != -1:
                break
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == peak_value:
                    return [i, j]