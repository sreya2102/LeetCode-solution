class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        brr=[]
        for i in nums:
            brr.append(i*i)
        brr.sort()
        return brr
