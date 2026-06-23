class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        brr=[]
        for ch in range(len(word)-1,-1,-1):
            brr.append(word[ch])
        a=" ".join(brr)
        return a
