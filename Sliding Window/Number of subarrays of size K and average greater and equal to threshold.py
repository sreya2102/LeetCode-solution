class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        brr=[]
        n=len(arr)
        for i in range(k):
            sum=sum+arr[i]
        av=sum//k
        if av>=threshold:
            brr.append(1)
        for i in range(1,n-k+1):
            sum=sum-arr[i-1]+arr[i+k-1]
            av=sum//k
            if av>=threshold:
                brr.append(1)
        return len(brr)

        
        