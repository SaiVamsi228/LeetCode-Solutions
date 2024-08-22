from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        hM = defaultdict(int)

        i = j = 0

        n = len(s)

        cnt = 0

        AtleOneOccur = 0

        while j < n :

            hM[s[j]] += 1

            if hM[s[j]] == 1:

                AtleOneOccur += 1
            
            if AtleOneOccur < 3:

                j += 1
            
            elif AtleOneOccur == 3:

                cnt += n - j #all upcoming strings are also valid substrings

                while AtleOneOccur == 3 and i < n :

                    hM[s[i]] -= 1

                    if hM[s[i]] == 0 :

                        AtleOneOccur -= 1
                    
                    if AtleOneOccur == 3:

                        cnt += n - j
                    
                    i += 1
                
                j += 1

        return cnt


