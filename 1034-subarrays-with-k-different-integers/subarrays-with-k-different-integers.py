from collections import defaultdict
class Solution:
    def getCntWithAtmostKDistinct(self,nums,k):
        hM = defaultdict(int)

        i = j = 0

        distCnt = 0

        n = len(nums)

        cnt = 0

        while j < n :

            hM[nums[j]] += 1

            if hM[nums[j]] == 1:

                distCnt += 1

            if distCnt <= k:

                cnt += j - i + 1

                j += 1
            
            elif distCnt > k :

                while i < n and distCnt > k and i <=j :

                    hM[nums[i]] -= 1

                    if hM[nums[i]] == 0:

                        distCnt -= 1
                    
                    i += 1
                
                if distCnt <= k :

                    cnt += j - i + 1

                j += 1
        
        return cnt

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        return self.getCntWithAtmostKDistinct(nums,k) - self.getCntWithAtmostKDistinct(nums,k-1)
        
                    


