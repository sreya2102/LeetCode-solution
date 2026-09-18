class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        queue=deque()
        queue.append([0])
        ans=[]
        while queue:
            path=queue.popleft()
            node=path[-1]
            for i in graph[node]:
                newpath=path+[i]
                if i==len(graph)-1:
                    ans.append(newpath)
                else:
                    queue.append(newpath)
        return ans
        