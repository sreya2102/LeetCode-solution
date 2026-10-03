class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        def bfs(x,y):
            dis=[-1]*10001
            dis[x]=0
            queue=deque()
            queue.append(x)
            while queue:
                x=queue.popleft()
                if x==y:
                    return dis[y]
                if x%11==0:
                    a=x//11
                    if 0<=a<=10000 and dis[a]==-1:
                        dis[a]=dis[x]+1
                        queue.append(a)
                if x%5==0:
                    b=x//5
                    if 0<=b<=10000 and dis[b]==-1:
                        dis[b]=dis[x]+1
                        queue.append(b)
                c=x-1
                if 0<=c<=10000 and dis[c]==-1:
                    dis[c]=dis[x]+1
                    queue.append(c)
                d=x+1
                if 0<=d<=10000 and dis[d]==-1:
                    dis[d]=dis[x]+1
                    queue.append(d)
        a=bfs(x,y)
        return a