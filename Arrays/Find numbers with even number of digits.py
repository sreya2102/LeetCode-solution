class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            c=0
            while(i>0):
                i=i//10
                c=c+1
            if c%2==0:
                a=a+1
        return a 
