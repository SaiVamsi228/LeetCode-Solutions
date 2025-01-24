class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        pos = -1

        # finding breaking point 

        for i in reversed(range(1,n)):

            if nums[i-1] < nums[i] :

                pos = i - 1

                break
        
        # no more pemutations possible
        if pos == -1:

            return nums.sort()
        
        # breaking point is found

        # fixing the left number : swap it with the first greater ele than breaking ele from right 

        for i in reversed(range(n)):

            if nums[i] > nums[pos]:

                nums[i], nums[pos] = nums[pos], nums[i]

                break
            
        # left ele is fixed now making the smallest possible number on the right 

        available_ele = nums[pos+1:].copy()

        available_ele.sort()

        for i in range(pos+1,n):

            nums[i] = available_ele[i-pos-1]
        
        return nums

        

        
