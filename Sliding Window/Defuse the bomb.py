class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0:
            return [0]*n
        ans=[0]*n
        if k>0:
            win=0
            for i in range(1,k+1):
                win=win+code[i%n]
            for i in range(n):
                ans[i]=win
                win=win-code[(i+1)%n]
                win=win+code[(i+k+1)%n]
        if k<0:
            k=-k
            win=0
            for i in range(n-k,n):
                win=win+code[i]
            for i in range(n):
                ans[i]=win
                win=win-code[(i-k+n)%n]
                win=win+code[i]
        return ans