class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        a=b=0
        found=0
        j=len(nums)
        while(i<j):
            if nums[i]==target:
                a=i
                found=1
                break
            else:
                i=i+1
        while(j!=0):
            if nums[j-1]==target:
                b=j
                found=1
                break
            else:
                j=j-1
        if found==1:
            return [a,b-1]
        else:
            return [-1,-1]
        