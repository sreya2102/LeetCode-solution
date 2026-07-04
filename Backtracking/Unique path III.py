class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count=0
        self.maxi=-1
        r=len(grid)
        c=len(grid[0])
        def find(i,j,a,sol,step):
            if i<0 or i>=r or j<0 or j>=c or a[i][j]==-1 or sol[i][j]==1:
                return False
            if a[i][j]==2:
                if step>self.maxi:
                    self.maxi=step
                    self.count=1
                elif self.maxi==step:
                    self.count=self.count+1
                return False
            sol[i][j]=1
            find(i - 1, j, a, sol, step + 1)
            find(i + 1, j, a, sol, step + 1)
            find(i, j - 1, a, sol, step + 1)
            find(i, j + 1, a, sol, step + 1)
            sol[i][j]=0
            return False
        d=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    x=i
                    y=j
        for i in range(r):
            for j in range(c):
                if grid[i][j]==-1:
                    d=d+1
        a=(r*c)-d
        sol=[[0]*c for _ in range(r)]
        find(x,y,grid,sol,0)
        if a==self.maxi+1:
            return self.count
        else:
            return 0

        
            
