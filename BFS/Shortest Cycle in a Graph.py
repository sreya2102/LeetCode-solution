class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans=float('inf')
        for s in range(n):
            queue=deque()
            queue.append(s)
            di=[-1]*n 
            par=[-1]*n
            di[s]=0
            while queue:
                node=queue.popleft()
                for i in adj[node]:
                    if di[i]==-1:
                        di[i]=di[node]+1
                        par[i]=node
                        queue.append(i)
                    elif par[node]!=i:
                        cy=di[node]+di[i]+1
                        ans=min(ans,cy)
        if ans==float('inf'):
            return -1
        else:
            return ans
