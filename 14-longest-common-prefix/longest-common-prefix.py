class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        q1 = deque([x for x in strs[0]])

        q2 = deque()

        n = len(strs)

        q1_turn = False # q1_turn => q1's turn to get filled

        for i in range(1,n):


            s = strs[i]

            if q1_turn == True: # q1's turn to get filled
                
                j = 0

                while q2 and j < len(s) and q2[0] == s[j] :

                    q1.append(q2.popleft())

                    j += 1
                
                q2 = deque()

                q1_turn = False
            
            elif q1_turn == False: # q2's turn to get filled

                j = 0

                while q1 and j < len(s) and q1[0] == s[j] :

                    q2.append(q1.popleft())

                    j += 1
                
                q1 = deque()

                q1_turn = True
        

        if q1 :

            return "".join(q1)
        
        else:

            return "".join(q2)





