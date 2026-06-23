class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen=s.lower()
        res=""
        for i in sen:
            if i.isalnum():
                res=res+i
        rev=res[::-1]
        return res==rev
