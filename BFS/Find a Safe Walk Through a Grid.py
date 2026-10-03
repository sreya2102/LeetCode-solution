class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        r=len(grid)
        c=len(grid[0])
        if grid[0][0]==1:
            health=health-1
        queue=deque()
        queue.append((0,0,health))
        v=set()
        v.add((0,0))
        while queue:
            i,j,health=queue.popleft()
            if i==r-1 and j==c-1:
                if health>=1:
                    return True
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<r and 0<=y<c and (x,y) not in v:
                    if grid[x][y]==0:
                        v.add((x,y))
                        queue.appendleft((x,y,health))
                    if grid[x][y]==1:
                        v.add((x,y))
                        queue.append((x,y,health-1))
        return False