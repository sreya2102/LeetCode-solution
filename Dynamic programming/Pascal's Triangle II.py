class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr=[]
        for i in range(1,rowIndex+2):
            val=1
            row=[]
            for j in range(1,i+1):
                row.append(val)
                val=val*(i-j)//j
            arr.append(row)
        return arr[rowIndex]
