class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=10**9
        dp=[[INF]*(amount+1) for _ in range(len(coins))]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
        for i in range(len(coins)):
            dp[i][0]=0
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
        if dp[len(dp)-1][len(dp[0])-1]==INF:
                return -1
        else:
            return dp[len(dp)-1][len(dp[0])-1]
        