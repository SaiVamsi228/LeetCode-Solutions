class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        target = 0

        n = len(nums)

        ans = set()

        nums.sort()

        for i in range(n):

            j = i + 1

            k = n - 1

            new_target = target - nums[i]

            while j < k:

                if nums[j] + nums[k] == new_target:

                    ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))

                    j += 1

                    k -= 1

                    while j < n and nums[j] == nums[j - 1]:

                        j += 1
                    
                    while k > 0 and nums[k] == nums[k+1]:

                        k -= 1 

                elif nums[j] + nums[k] > new_target:

                    k -= 1
                
                elif nums[j] + nums[k] < new_target:

                    j += 1
            
        
        return list(ans)
