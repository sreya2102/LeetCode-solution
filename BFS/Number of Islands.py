class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    count=count+1
                    queue=deque()
                    queue.append((i,j))
                    grid[i][j]="0"
                    while queue:
                        x,y=queue.popleft()
                        for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if 0<=a<r and 0<=b<c:
                                if grid[a][b]=="1":
                                    queue.append((a,b))
                                    grid[a][b]="0"
        return count
