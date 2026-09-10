class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(dp)):
            if i==1:
                dp[i]=max(nums[i],dp[i-1])
            else:
                dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[len(dp)-1]