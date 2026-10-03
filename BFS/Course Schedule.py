class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        inde=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            inde[u]+=1
        queue=deque()
        for i in range(numCourses):
            if inde[i]==0:
                queue.append(i)
        v=set()
        v.add(0)
        count=0
        while queue:
            node=queue.popleft()
            count=count+1
            for i in adj[node]:
                inde[i]-=1
                if inde[i]==0:
                    queue.append(i)
        return count==numCourses