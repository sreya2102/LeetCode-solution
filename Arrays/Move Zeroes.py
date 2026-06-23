class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        m=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[m]=nums[i]
                m=m+1
        while(m<len(nums)):
            nums[m]=0
            m=m+1
            
        
