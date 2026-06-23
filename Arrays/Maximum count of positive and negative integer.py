class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        a=0
        for i in nums:
            if i>0:
                c=c+1
        for i in nums:
            if i<0:
                a=a+1
        if c>a:
            return c
        return a
