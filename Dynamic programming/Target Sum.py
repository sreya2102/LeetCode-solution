class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot=sum(nums)
        if abs(target)>tot:
            return 0
        if (target+tot)%2!=0:
            return 0
        r=(target+tot)//2
        dp=[0]*(r+1)
        dp[0]=1
        for i in nums:
            for s in range(r,i-1,-1):
                dp[s]=dp[s]+dp[s-i]
        return dp[r]

            

        