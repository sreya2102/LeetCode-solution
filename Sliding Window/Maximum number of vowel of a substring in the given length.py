class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        n=len(s)
        for i in range(k):
            if s[i] in 'aeiou':
                c=c+1
        ma=c
        for i in range(1,n-k+1):
            if s[i-1] in 'aeiou':
                c=c-1
            if s[i+k-1] in 'aeiou':
                c=c+1
            if c>ma:
                ma=c
        return ma