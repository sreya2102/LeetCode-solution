class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=list(set(nums))
        brr=[]
        a.sort()
        if len(a)<3:
            return max(a)
        else:
            for i in range(len(a),0,-1):
                brr.append(a[i-1])
            return brr[2]
