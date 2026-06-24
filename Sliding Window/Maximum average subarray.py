class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        brr=[]
        n=len(nums)
        sum=0
        for i in range(k):
            sum=sum+nums[i]
        a=sum/k
        ma=a
        for i in range(1,n-k+1):
            sum=sum-nums[i-1]+nums[i+k-1]
            a=sum/k
            if a>ma:
                ma=a
        return ma