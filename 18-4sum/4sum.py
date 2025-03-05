class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = set()

        n = len(nums)

        nums.sort()

        for i in range(n):

            for j in range(i+1,n):
                
                first,second = nums[i],nums[j]

                new_target = target - (first + second)

                left = j + 1

                right = n - 1

                while left < right:

                    if nums[left] + nums[right] == new_target:

                        ans.add((first,second,nums[left],nums[right]))

                        left += 1

                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif nums[left] + nums[right] > new_target:

                        right -= 1
                    
                    elif nums[left] + nums[right] < new_target:

                        left += 1
                
        
        return list(ans)
                    
