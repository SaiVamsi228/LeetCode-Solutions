class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Brute

        hash_set = set()

        for num in nums:

            if num in hash_set:

                return num
            
            hash_set.add(num)
        
        return -1
