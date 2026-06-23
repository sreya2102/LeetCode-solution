class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if c==0:
                seen=i
            if i==seen:
                c=c+1
            else:
                c=c-1
        return seen
