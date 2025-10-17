class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        q = deque()

        q.append(beginWord)

        step = 1

        wordList = set(wordList)

        hs = set()

        hs.add(beginWord)

        hm = {}

        min_step = 0

        while q:
                        
            t = len(q)

            step += 1

            for _ in range(t):
                
                word = q.popleft()

                hm[word] = step

                for i,char in enumerate(word):

                    for new_letter in "abcdefghijklmnopqrstuvwxyz":

                        if char == new_letter:

                            continue
                        
                        new_word = word[:i] + new_letter + word[i+1:]

                        if new_word in hs:

                            continue
                        
                        if new_word in wordList:

                            hs.add(new_word)

                            q.append(new_word)
                            
                            if new_word == endWord:

                                min_step = step

                                break

        ans = []

        print(min_step)

        if min_step == 0:

            return ans

        def genSequences(src,dest,path):

            nonlocal min_step

            if src == dest:

                if len(path) == min_step:
                    
                    flow = path.copy()[::-1]

                    ans.append(flow)

                return
            
            word = src

            for i,char in enumerate(word):

                for new_letter in "abcdefghijklmnopqrstuvwxyz":

                    if char == new_letter:

                        continue
                    
                    new_word = word[:i] + new_letter + word[i+1:]

                    if new_word in path:

                        continue
                    
                    elif new_word in hm and hm[new_word] == hm[word] - 1:

                        path.append(new_word)

                        genSequences(new_word,dest,path)

                        path.pop()

        genSequences(endWord,beginWord,[endWord])

        return ans
        


                        
                        
            





