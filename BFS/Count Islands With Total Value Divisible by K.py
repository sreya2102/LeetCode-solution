class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=0:
                    sum=grid[i][j]
                    queue=deque()
                    queue.append((i,j))
                    grid[i][j]=0
                    while queue:
                        x,y=queue.popleft()
                        for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if 0<=a<r and 0<=b<c:
                                if grid[a][b]!=0:
                                    sum=sum+grid[a][b]
                                    queue.append((a,b))
                                    grid[a][b]=0
                    if sum%k==0:
                        count=count+1
        return count