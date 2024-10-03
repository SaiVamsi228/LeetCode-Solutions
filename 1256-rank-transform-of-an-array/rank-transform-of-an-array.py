class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        newArr = arr.copy()

        newArr.sort()

        mp = {}

        r = 1 

        for i,ele in enumerate(newArr):

            if i > 0 and newArr[i] != newArr[i-1]:

                r += 1

            mp[ele] = r
        
        for i in range(len(arr)):

            arr[i] = mp[arr[i]]
        
        return arr
            
