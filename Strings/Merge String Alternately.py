class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=word1
        t=word2
        brr=[]
        i=0
        while(i<len(s) or i<len(t)):
            if i<len(s) and i<len(t):
                brr.append(s[i])
                brr.append(t[i])
                i=i+1
            elif i<len(s):
                brr.append(s[i])
                i=i+1
            elif i<len(t):
                brr.append(t[i])
                i=i+1
        a="".join(brr)
        return a
