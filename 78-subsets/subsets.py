class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        bin_str = "1"*n

        int_val = int(bin_str,2)

        subsets = []

        for num in range(int_val + 1):

            subset = []

            for j in range(n):

                if num & 1 :

                    subset.append(nums[j])
                
                num >>= 1
            
            subsets.append(subset)
    
        return subsets
                




        