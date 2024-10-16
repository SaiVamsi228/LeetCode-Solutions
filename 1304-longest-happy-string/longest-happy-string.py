class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        hp = []

        heapify(hp)

        if a != 0:

            heappush(hp, (-a, "a"))
        
        if b != 0 :

            heappush(hp, (-b,"b"))
        
        if c != 0:

            heappush(hp, (-c, "c" ))
        
        s = []

        consec = {"a": 0 , "b": 0 ,"c": 0}
            
        while hp:

            cnt, curEle = heappop(hp)

            cnt *= -1

            if consec[curEle] == 0:

                if cnt >= 2:

                    cnt -= 2

                    s.append(curEle)

                    s.append(curEle)

                    consec = {"a": 0 , "b": 0 ,"c": 0}

                    consec[curEle] = 2

                    
                
                elif cnt >= 1 :

                    cnt -= 1

                    s.append(curEle)

                    consec = {"a": 0 , "b": 0 ,"c": 0}

                    consec[curEle] = 1
                
                if cnt:
                        
                    heappush(hp, (-cnt, curEle))
            
            elif consec[curEle] == 1:

                if cnt > 0 :

                    cnt -= 1

                    s.append(curEle)

                    consec = {"a": 0 , "b": 0 ,"c": 0}

                    consec[curEle] = 2

                if cnt :

                    heappush(hp,(-cnt, curEle))
            
            elif consec[curEle] == 2:

                if not hp:

                    break

                newCnt, newEle = heappop(hp)
                
                newCnt *= -1

                heappush(hp, (-cnt, curEle))

                consec[curEle] = 0

                newCnt -= 1

                s.append(newEle)

                consec = {"a": 0 , "b": 0 ,"c": 0}

                consec[newEle] = 1

                if newCnt:

                    heappush(hp, (-newCnt, newEle))
        
        return "".join(s)

