class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        brr=[]
        def subsets(index,nums,subset):
            if index==len(nums):
                brr.append(subset[:])
                return 
            subset.append(nums[index])
            subsets(index+1,nums,subset)
            subset.pop()
            subsets(index+1,nums,subset)
        subsets(0,nums,[])
        return brr