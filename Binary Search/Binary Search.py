class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        low=0
        high=len(nums)-1
        found=0
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                found=1
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if found==0:
            return -1
        
