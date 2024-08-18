class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zeroCnt = k

        i = j = 0

        n = len(nums)

        mx = 0

        while j < n:

            if nums[j] == 0:

                zeroCnt -= 1

            if zeroCnt >= 0: #as since atmost k bits

                mx = max(mx, j-i+1)
            
                j += 1
            
            elif zeroCnt < 0:

                while zeroCnt < 0:

                    if nums[i] == 0 :

                        zeroCnt += 1

                    i+=1
                
                j += 1
        
        return mx

