class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        for i in range(1,numRows+1):
            val=1
            row=[]
            for j in range(1,i+1):
                row.append(val)
                val=val*(i-j)//j
            arr.append(row)
        return arr
