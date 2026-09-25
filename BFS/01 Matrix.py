class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        r=len(mat)
        c=len(mat[0])
        queue=deque()
        di=[[-1]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    queue.append((i,j))
                    di[i][j]=0
        while queue:
            i,j=queue.popleft()
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<r and 0<=y<c:
                    if di[x][y]==-1:
                        di[x][y]=di[i][j]+1
                        queue.append((x,y))
        return di
                