class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a=len(nums)
        for i in range(a):
            if i!=nums[i]:
                return i
        return a
