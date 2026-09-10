class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        crr=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            crr=max(nums[i],crr+nums[i])
            maxi=max(maxi,crr)
        return maxi