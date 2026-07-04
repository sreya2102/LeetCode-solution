arr=list(map(int,input().split()))
arr.sort()
tar=int(input())
brr=[]
sol=[0]*len(arr)
def find(index,currentsum):
    if currentsum==tar:
        temp=[]
        for i in range(len(sol)):
            if sol[i]==1:
                temp.append(arr[i])
        brr.append(temp)
        return 
    if index>=len(arr):
        return
    if currentsum>tar:
        return 
    sol[index]=1
    find(index+1,currentsum+arr[index])
    sol[index]=0
    nextindex=index
    while nextindex+1<len(arr) and arr[nextindex]==arr[nextindex+1]:
        nextindex=nextindex+1
    find(nextindex+1,currentsum)
find(0,0)
print(brr)