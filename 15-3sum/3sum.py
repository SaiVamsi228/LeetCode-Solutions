class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        n = len(nums)

        ans = set()

        nums.sort()

        for i in range(n):

            left, right = i + 1 , n - 1

            first = nums[i]

            target = -first

            while left < right :

                if nums[left] + nums[right]  == target:

                    triplet = [first,nums[left], nums[right]]

                    ans.add(tuple(triplet))

                    left += 1

                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:

                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:

                        right -= 1

                elif nums[left] + nums[right] < target:

                    left += 1
                
                elif nums[left] + nums[right] > target:

                    right -= 1
            

        return list(ans)