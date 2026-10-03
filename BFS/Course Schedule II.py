class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj=[[] for _ in range(numCourses)]
        inde=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            inde[u]+=1
        ans=[]
        queue=deque()
        for i in range(numCourses):
            if inde[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
            ans.append(node)
            for i in adj[node]:
                inde[i]-=1
                if inde[i]==0:
                    queue.append(i)
        if len(ans)==numCourses:
            return ans
        else:
            return []
            
            