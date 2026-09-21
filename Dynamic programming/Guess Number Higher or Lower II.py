class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp=[[0]*(n+2) for _ in range(n+2)]
        for i in range(n-1,0,-1):
            for j in range(i+1,n+1):
                ans=10**9
                for k in range(i,j+1):
                    if k==i:
                        cost=k+dp[k+1][j]
                    elif k==j:
                        cost=k+dp[i][k-1]
                    else:
                        cost=k+max(dp[i][k-1],dp[k+1][j])
                    if cost<ans:
                        ans=cost
                dp[i][j]=ans
        return dp[1][n]