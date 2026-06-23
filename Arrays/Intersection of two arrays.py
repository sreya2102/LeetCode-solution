class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        brr=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                brr.append(nums1[i])
        s=list(set(brr))
        return s

        