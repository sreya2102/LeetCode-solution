class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def find(s,o,c):
            nonlocal result
            if o==n and c==n:
                result.append(s)
                return
            if o<n:
                find(s+"(",o+1,c)
            if c<o:
                find(s+")",o,c+1)
        find("",0,0)
        return result
