class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        fr1=[0]*26
        fr2=[0]*26
        k=len(s1)
        n=len(s2)
        found=0
        for i in range(len(s1)):
            fr1[ord(s1[i])-ord('a')]+=1
        for i in range(len(s1)):
            fr2[ord(s2[i])-ord('a')]+=1
        if fr1==fr2:
            return True
        else:
            for i in range(1,n-k+1):
                fr2[ord(s2[i-1])-ord('a')]-=1
                fr2[ord(s2[i+k-1])-ord('a')]+=1
                if fr1==fr2:
                    found=1
                    break
            if found==1:
                return True
            else:
                return False