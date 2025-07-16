class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1,n2,c1,c2 = None, None , 0, 0

        for num in nums:

            if num == n1:

                c1 += 1
            
            elif num == n2:

                c2 += 1
            
            elif c1 == 0:

                n1 = num

                c1 = 1
            
            elif c2 == 0:

                n2 = num

                c2 = 1
            
            else:

                c1 -= 1

                c2 -= 1
        

        act_cnt_1 = act_cnt_2 = 0

        for num in nums:

            if num == n1 :

                act_cnt_1 += 1

            elif num == n2:

                act_cnt_2 += 1

        ans = []

        n = len(nums)

        if act_cnt_1 > n//3:

            ans.append(n1)

        if act_cnt_2 > n//3:

            ans.append(n2)

        return ans