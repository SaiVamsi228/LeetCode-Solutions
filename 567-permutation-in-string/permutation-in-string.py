class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        mp = defaultdict(int)

        for char in s1:

            mp[char] += 1
        
        distCnt = len(mp)

        n = len(s2)

        k = len(s1)

        i = 0

        j = 0

        while j < n:

            char = s2[j]

            if char in mp and mp[char] == 0 :

                while mp[char] == 0:

                    if s2[i] in mp :
                        
                        mp[s2[i]] += 1

                        if mp[s2[i]] == 1:

                            distCnt += 1
                    
                    i += 1

            if char in mp and mp[char] > 0:

                mp[char] -= 1

                if mp[char] == 0:

                    distCnt -= 1
                
                if distCnt == 0:

                    return True
                
                j += 1


            else:

                while i <= j :

                    if s2[i] in mp :
                        
                        mp[s2[i]] += 1

                        if mp[s2[i]] == 1:

                            distCnt += 1
                    
                    i += 1
                
                j += 1

                i = j
        
        return False


                    




            # if j - i + 1 < k :



