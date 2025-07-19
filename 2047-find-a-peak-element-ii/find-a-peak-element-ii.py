class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        left = 0
        right = m - 1

        while left <= right:
            mid = (left + right) // 2

            # Find the row with the maximum value in mid column
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Get left and right neighbors
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < m else -1

            # Check if it is a peak
            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row, mid]
            elif mat[max_row][mid] < right_val:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]  # shouldn't be reached
