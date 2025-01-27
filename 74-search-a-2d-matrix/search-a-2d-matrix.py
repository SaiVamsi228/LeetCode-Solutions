class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)

        n = len(matrix[0])

        def search1D(arr,target):

            low = 0

            high = n - 1

            while low <= high :

                mid = (low+high)//2

                if arr[mid] == target:

                    return True
                
                elif arr[mid] > target:

                    high = mid - 1
                
                else:

                    low = mid + 1
            
            return False
        
        for i in range(m):

            if matrix[i][0] <= target <= matrix[i][-1] and search1D(matrix[i],target):

                return True
        
        return False

