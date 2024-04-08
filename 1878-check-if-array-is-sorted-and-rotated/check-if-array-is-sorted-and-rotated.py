class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n==1:
            return True

        rotate_chance = False
        for i in range(1,n):

            if nums[i] < nums[i-1] :

                if not rotate_chance :

                    rotate_chance = True

                else:
                    return False
        
        if rotate_chance and nums[n-1] > nums[0]:

            return False
        
        return True