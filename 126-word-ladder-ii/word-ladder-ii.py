from collections import deque, defaultdict

class Solution:
    def __init__(self):
        self.mp = {}

    def dfs(self, endWord, beginWord, vec, path):
        if endWord == beginWord:
            vec.append(path[::-1])
            return
        for i in range(len(endWord)):
            temp = list(endWord)
            for c in 'abcdefghijklmnopqrstuvwxyz':
                temp[i] = c
                next_word = ''.join(temp)
                if next_word in self.mp and self.mp[next_word] + 1 == self.mp[endWord]:
                    path.append(next_word)
                    self.dfs(next_word, beginWord, vec, path)
                    path.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        q = deque()
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        word_set.discard(beginWord)
        q.append(beginWord)
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                word = q.popleft()
                self.mp[word] = level
                for i in range(len(word)):
                    temp = list(word)
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        temp[i] = c
                        next_word = ''.join(temp)
                        if next_word in word_set:
                            q.append(next_word)
                            word_set.remove(next_word)

        result = []
        if endWord in self.mp:
            self.dfs(endWord, beginWord, result, [endWord])
        return result
