class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        hash_map = {}

        for i in range(n):

            if nums[i] not in hash_map:

                hash_map[nums[i]] = 1
            
            else:

                hash_map[nums[i]]+=1
        

        for num, cnt in hash_map.items():

            if cnt == 1:

                return num
            