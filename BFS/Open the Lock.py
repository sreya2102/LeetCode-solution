class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        else:
            queue=deque()
            queue.append(("0000",0))
            v=set()
            v.add("0000")
            while queue:
                curr,step=queue.popleft()
                if curr==target:
                    return step
                for i in range(4):
                    arr=list(curr)
                    if arr[i]=='9':
                        arr[i]='0'
                    else:
                        arr[i]=str(int(arr[i])+1)
                    nextstate=''.join(arr)
                    if nextstate not in v and nextstate not in deadends:
                        queue.append((nextstate,step+1))
                        v.add(nextstate)
                    arr=list(curr)
                    if arr[i]=='0':
                        arr[i]='9'
                    else:
                        arr[i]=str(int(arr[i])-1)
                    nextstate=''.join(arr)
                    if nextstate not in v and nextstate not in deadends:
                        v.add(nextstate)
                        queue.append((nextstate,step+1))
            return -1
            