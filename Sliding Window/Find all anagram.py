class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        fr1=[0]*26
        fr2=[0]*26
        brr=[]
        k=len(p)
        for i in range(len(p)):
            fr1[ord(p[i])-ord('a')]+=1
        for i in range(k):
            fr2[ord(s[i])-ord('a')]+=1
        if fr1==fr2:
            brr.append(i-len(p)+1)
        for i in range(1,len(s)-len(p)+1):
            fr2[ord(s[i-1])-ord('a')]-=1
            fr2[ord(s[i+k-1])-ord('a')]+=1
            if fr1==fr2:
                brr.append(i)
        return brr
        
