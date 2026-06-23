class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        a=""
        for i in words:
            if i[::-1]==i:
                a=a+i
                break
        return a
