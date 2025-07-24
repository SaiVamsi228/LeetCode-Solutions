class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []

        def isPalin(s):

            return s == s[::-1]

        def getAllPalPart(start,path):

            if start == n :

                ans.append(path.copy())

                return
            
            for end in range(start,n):

                sub_str = s[start:end+1]

                if isPalin(sub_str):

                    path.append(sub_str)

                    getAllPalPart(end+1,path)

                    path.pop()
        
        n = len(s)

        getAllPalPart(0,[])

        return ans