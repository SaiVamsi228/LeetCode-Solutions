class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = j = 0

        hashSet = set()

        mx = 0

        n = len(s)

        uniqueCnt = 0

        k = 0 #IMP as no repeating char

        mx = 0
        while j < n:

            if s[j] not in hashSet :

                uniqueCnt += 1
            
            hashSet.add(s[j])


            if j-i+1 - uniqueCnt == k:

                mx = max(mx, j-i+1)

                j += 1

            elif j-i+1 - uniqueCnt > k : #there exists repeating char

                repeatedEle = s[j]

                while s[i] != repeatedEle:
                    
                    hashSet.remove(s[i])

                    uniqueCnt -= 1

                    i += 1
                
                i+=1
                
                j += 1
        
        return mx
