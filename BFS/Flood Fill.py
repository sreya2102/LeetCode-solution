from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r=len(image)
    
        c=len(image[0])
        old=image[sr][sc]
        image[sr][sc]=color
        queue=deque()
        queue.append((sr,sc))
        v=[[False]*c for _ in range(r)]
        v[sr][sc]=True
        while queue:
            i,j=queue.popleft()
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<r and 0<=y<c and not v[x][y]:
                    if image[x][y]==old:
                        image[x][y]=color
                        v[x][y]=True
                        queue.append((x,y))
        return image
            