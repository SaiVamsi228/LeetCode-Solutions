class Solution:
    def solve(self, nums, n, k):

        cnt = 0

        n = len(nums)

        i = j = 0

        odd = 0
        
        while j < n :

            if nums[j] % 2 == 1:

                odd += 1
            
            while odd > k and i <= j and i<n :

                if nums[i] % 2 == 1:

                    odd -= 1

                i += 1
            
            if odd <= k:
                
                cnt += j - i + 1

            j += 1
        
        return cnt

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        return self.solve(nums,n,k) - self.solve(nums,n,k-1)



