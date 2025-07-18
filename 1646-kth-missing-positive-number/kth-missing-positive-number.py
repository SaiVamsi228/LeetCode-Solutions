class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        n = len(arr)

        left = 0

        right = n - 1

        while left <= right:


            cur_ind = (left + right)//2

            missing_cnt = arr[cur_ind] - cur_ind - 1

            # we are trying to eliminate the search space where we can find the kth missing
            if missing_cnt < k :

                left = cur_ind + 1
            
            else:

                right = cur_ind - 1
        
        return left + k 




