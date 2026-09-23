class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord==endWord:
            return 1
        patterns={}
        for word in wordList:
            for i in range(len(word)):
                k=word[:i]+"*"+word[i+1:]
                if k not in patterns:
                    patterns[k]=[]
                patterns[k].append(word)
        queue=deque()
        queue.append(beginWord)
        v=set()
        v.add(beginWord)
        dist=1
        while queue:
            for _ in range(len(queue)):
                word=queue.popleft()
                if word==endWord:
                    return dist
                for i in range(len(word)):
                    k=word[:i]+"*"+word[i+1:]
                    if k not in patterns:
                        continue
                    for j in patterns[k]:
                        if j not in v:
                            v.add(j)
                            queue.append(j)
                    patterns[k]=[]
                    
            dist=dist+1
        return 0