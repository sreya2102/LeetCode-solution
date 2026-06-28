class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s=blocks
        n=len(s)
        c=0
        for i in range(k):
            if s[i]=='W':
                c=c+1
        mi=c
        for i in range(1,n-k+1):
            if s[i-1]=='W':
                c=c-1
            if s[i+k-1]=='W':
                c=c+1
            if c<mi:
                mi=c
        return mi