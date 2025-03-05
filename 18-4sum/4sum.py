class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = set()

        n = len(nums)

        for i in range(n):

            for j in range(i+1,n):

                seen = set() # using the for loop to get fourth

                for k in range(j+1,n):

                    first, second, third = nums[i], nums[j], nums[k]

                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in seen:

                        quad = [first, second, third, fourth]

                        quad.sort()
                    
                        ans.add(tuple(quad))

                    seen.add(third)
        
        return list(ans)
                    
