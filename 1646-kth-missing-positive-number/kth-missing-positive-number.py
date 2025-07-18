class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        start = 1

        missing_cnt = 0

        n = len(arr)

        i = 0

        while i < n and missing_cnt != k:

            if start == arr[i]:

                i += 1
            
            else:

                missing_cnt += 1
            
            if missing_cnt == k:

                return start
            
            start += 1
        
        return start + k - missing_cnt - 1
        


