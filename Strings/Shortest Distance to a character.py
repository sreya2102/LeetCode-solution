class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos=[]
        for i in range(len(s)):
            if s[i]==c:
                pos.append(i)
        brr=[]
        for i in range(len(s)):
            mini=float('inf')
            for p in pos:
                mini=min(mini,abs(i-p))
            brr.append(mini)
        return brr