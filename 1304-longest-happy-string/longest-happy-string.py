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
            
        while hp:

            cnt, curEle = heappop(hp)

            cnt *= -1

            if len(s) >= 2  :

                firstPrev = s[-1]

                secondPrev = s[-2]

                if firstPrev == secondPrev == curEle:

                    if not hp:

                        break

                    tempCnt, tempEle = heappop(hp)

                    tempCnt *= -1

                    tempCnt -= 1

                    s.append(tempEle)

                    if tempCnt:
                        
                        heappush(hp,(-tempCnt, tempEle))


                elif curEle == firstPrev :

                    s.append(curEle)

                    cnt -= 1

                else:

                    if cnt >= 2 :

                        cnt -= 2

                        s.append(curEle)

                        s.append(curEle)
                    
                    elif cnt == 1:

                        cnt -= 1

                        s.append(curEle)

                if cnt :

                    heappush(hp, (-cnt, curEle ))

            else:

                if cnt >= 2 :

                    cnt -= 2

                    s.append(curEle)

                    s.append(curEle)
                
                elif cnt == 1:

                    cnt -= 1

                    s.append(curEle)

                if cnt :

                    heappush(hp, (-cnt, curEle ))

        return "".join(s)

