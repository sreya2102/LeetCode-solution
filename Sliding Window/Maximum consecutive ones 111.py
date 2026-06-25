class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxi=0
        z=0
        r=0
        while(r<len(nums)):
            if nums[r]==0:
                z=z+1
            while(z>k):
                if nums[l]==0:
                    z=z-1
                l=l+1
            if z<=k:
                maxi=max(maxi,r-l+1)
            r=r+1
        return maxi