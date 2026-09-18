class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue=deque()
        queue.append(source)
        di=[-1]*n
        di[source]=1
        while queue:
            node=queue.popleft()
            for i in adj[node]:
                if di[i]==-1:
                    di[i]=di[node]+1
                    queue.append(i)
        if di[destination]==-1:
            return False
        else:
            return True