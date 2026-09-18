class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        v=set()  
        count=0      
        for s in range(n):
            if s not in v:
                queue=deque()
                queue.append(s)
                v.add(s)
                nodecount=0
                edge=0
                while queue:
                    node=queue.popleft()
                    nodecount=nodecount+1
                    for i in adj[node]:
                        edge=edge+1
                        if i not in v:
                            v.add(i)
                            queue.append(i)
                edge=edge//2
                if edge==nodecount*(nodecount-1)//2:
                    count=count+1
        return count
                

