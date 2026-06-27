class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1=nums1
        arr2=nums2
        brr=[]
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i]==arr2[j]:
                    if j==len(arr2)-1:
                        brr.append(-1)
                        break
                    if arr2[j]<arr2[j+1]:
                        brr.append(arr2[j+1])
                        break
                    else:
                        ma=arr2[j]
                        for k in range(j+1,len(arr2)):
                            if arr2[j]<arr2[k]:
                                ma=arr2[k]
                                brr.append(ma)
                                break
                        else:
                            brr.append(-1)
                            break
        return brr
