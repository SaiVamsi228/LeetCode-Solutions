class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        n = len(nums)

        nums.sort()

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            a = nums[i]
            
            hs = set()
            
            for j in range(i+1,n):
                
                b = nums[j]

                c = -1*(a+b)
                
                if c in hs:

                    ans_set = [a,c,b]

                    ans.add(tuple(sorted(ans_set)))
                
                hs.add(b)
        
        return list(ans)
                