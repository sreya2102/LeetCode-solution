class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        fre=[0]*(max(nums)+1)
        brr=[]
        for i in nums:
            fre[i]+=1
        for i in range(len(fre)):
            a=i*fre[i]
            brr.append(a)
        dp=[0]*(len(brr))
        dp[0]=brr[0]
        for i in range(1,len(brr)):
            if i==1:
                dp[i]=max(dp[i-1],brr[i])
            else:
                dp[i]=max(dp[i-1],brr[i]+dp[i-2])
        return dp[len(dp)-1]
        