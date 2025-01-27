class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        majority_1 = majority_2 = -1

        cnt_1 = cnt_2 = 0

        for num in nums:

            if num == majority_1:

                cnt_1 += 1
            
            elif num == majority_2 :

                cnt_2 += 1
            
            elif cnt_1 == 0 :

                majority_1 = num

                cnt_1 = 1
            
            elif cnt_2 == 0:

                majority_2 = num

                cnt_2 = 1
            
            else:

                cnt_1 -= 1

                cnt_2 -= 1

        act_cnt_1 = act_cnt_2 = 0

        for num in nums:

            if num == majority_1 :

                act_cnt_1 += 1

            elif num == majority_2:

                act_cnt_2 += 1
                
        n = len(nums)
        
        if act_cnt_1 > n//3 and act_cnt_2 > n//3:

            return [majority_1,majority_2]
        
        elif act_cnt_1 > n//3 :

            return [majority_1]
        
        elif act_cnt_2 > n//3:

            return [majority_2]
        
        else:

            return []
