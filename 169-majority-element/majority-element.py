class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        ele_cnt = 0

        for num in nums:

            if not ele_cnt :

                ele = num

                ele_cnt = 1

            elif num == ele:

                ele_cnt += 1
            
            else:

                ele_cnt -= 1

        return ele
        

