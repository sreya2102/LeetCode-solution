class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        def back(p,u):
            if len(p)==len(nums):
                arr.append(p[:])
                return
            for i in range(len(nums)):
                if not u[i]:
                    u[i]=True
                    p.append(nums[i])
                    back(p,u)
                    p.pop()
                    u[i]=False
        back([],[False]*len(nums))
        return arr
        