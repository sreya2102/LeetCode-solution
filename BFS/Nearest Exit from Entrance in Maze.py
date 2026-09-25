class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        r=len(maze)
        c=len(maze[0])
        s,s1=entrance[0],entrance[1]
        queue=deque()
        queue.append((s,s1,0))
        v=set()
        v.add((s,s1))
        while queue:
            i,j,m=queue.popleft()
            if (i,j)!=(s,s1) and ((i==0 or i==r-1) or (j==0 or j==c-1)) and maze[i][j]=='.':
                return m
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<r and 0<=y<c and (x,y) not in v and maze[x][y]!='+':
                    v.add((x,y))
                    queue.append((x,y,m+1))
        return -1