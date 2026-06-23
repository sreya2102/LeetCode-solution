class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=list(s)
        i=0
        j=len(arr)-1
        while(i<j):
            if arr[i] in "aeiouAEIOU" and arr[j] in "aeiouAEIOU":
                arr[i],arr[j]=arr[j],arr[i]
                i=i+1
                j=j-1
            elif arr[i] not in "aeiouAEIOU":
                i=i+1
            else:
                j=j-1
        s="".join(arr)
        return s
