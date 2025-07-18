class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        n = len(arr)

        left = 0

        right = n - 1

        ans = -1

        while left <= right:

            mid = (left + right)//2

            if arr[mid] == target :

                ans = mid 

                break

            if arr[left] < arr[mid] < arr[right]:

                # we are in the sorted one
                if arr[mid] > target :

                    right = mid - 1
                
                else:

                    left = mid + 1
            
            elif arr[left] <= arr[mid] >= arr[right]:

                # sorted is on left

                if arr[left] <= target <= arr[mid]:

                    right = mid - 1
                
                else:

                    left = mid + 1


            
            elif arr[left] >= arr[mid] <= arr[right] :

                # sorted is on right

                if arr[mid] <= target <= arr[right]:

                    left = mid + 1
                
                else:

                    right = mid - 1

        return ans





            