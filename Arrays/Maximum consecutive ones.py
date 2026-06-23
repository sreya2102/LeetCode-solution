class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        ma=0
        for i in nums:
            if i==1:
                c=c+1
            elif i==0:
                c=0
            if c>ma:
                ma=c
        return ma