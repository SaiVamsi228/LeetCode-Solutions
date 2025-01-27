class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)

        n = len(matrix[0])

        low = 0

        high = m*n - 1

        while low <= high:

            mid = (low + high)//2

            mid_row, mid_col = divmod(mid,n)

            mid_ele = matrix[mid_row][mid_col]

            if  mid_ele == target:

                return True
            
            elif target < mid_ele:

                high = mid - 1
            
            elif target > mid_ele:

                low = mid + 1
        
        return False

                