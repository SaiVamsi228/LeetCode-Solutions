class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = 0

        cnt_ele = -1

        for num in nums:

            if cnt == 0:

                cnt_ele = num

                cnt += 1
            
            elif  num == cnt_ele:

                cnt += 1
            
            else:

                cnt -= 1
        
        return cnt_ele

