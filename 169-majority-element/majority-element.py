class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj_ele = None

        maj_cnt = 0

        for num in nums:

            if maj_cnt == 0:

                maj_ele = num

                maj_cnt = 1
            
            elif maj_ele == num:

                maj_cnt += 1
            
            else:

                maj_cnt -= 1
            
        return maj_ele

