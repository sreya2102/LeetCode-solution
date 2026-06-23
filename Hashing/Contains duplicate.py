class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        m=set(nums)
        a=len(m)
        if n!=a:
            return True
        return False
