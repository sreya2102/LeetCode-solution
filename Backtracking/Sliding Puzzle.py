from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        tar=[[1,2,3],[4,5,0]]
        r=len(board)
        c=len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j]==0:
                    x,y=i,j
        queue=deque()
        m=0
        queue.append((board,m))
        vq=deque()
        vq.append(board)
        if x-1>=0:
            brr=[row[:] for row in board]
            temp=brr[x-1][y]
            brr[x-1][y]=brr[x][y]
            brr[x][y]=temp
            queue.append((brr,m+1))
        if x+1<=r-1:
            brr=[row[:] for row in board]
            temp=brr[x+1][y]
            brr[x+1][y]=brr[x][y]
            brr[x][y]=temp
            queue.append((brr,m+1))
        if y-1>=0:
            brr=[row[:] for row in board]
            temp=brr[x][y-1]
            brr[x][y-1]=brr[x][y]
            brr[x][y]=temp
            queue.append((brr,m+1))
        if y+1<=c-1:
            brr=[row[:] for row in board]
            temp=brr[x][y+1]
            brr[x][y+1]=brr[x][y]
            brr[x][y]=temp
            queue.append((brr,m+1))
        while queue:
            state,m=queue.popleft()
            if state==tar:
                return m
                exit()
            if state in vq:
                continue
            vq.append(state)
            for i in range(r):
                for j in range(c):
                    if state[i][j]==0:
                        x,y=i,j
            if x-1>=0:
                brr=[row[:] for row in state]
                temp=brr[x-1][y]
                brr[x-1][y]=brr[x][y]
                brr[x][y]=temp
                queue.append((brr,m+1))
            if x+1<=r-1:
                brr=[row[:] for row in state]
                temp=brr[x+1][y]
                brr[x+1][y]=brr[x][y]
                brr[x][y]=temp
                queue.append((brr,m+1))
            if y-1>=0:
                brr=[row[:] for row in state]
                temp=brr[x][y-1]
                brr[x][y-1]=brr[x][y]
                brr[x][y]=temp
                queue.append((brr,m+1))
            if y+1<=c-1:
                brr=[row[:] for row in state]
                temp=brr[x][y+1]
                brr[x][y+1]=brr[x][y]
                brr[x][y]=temp
                queue.append((brr,m+1))
        return -1
            
            

