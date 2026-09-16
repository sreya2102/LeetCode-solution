from collections import deque
from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target>x+y:
            return False
        if target % gcd(x,y)!=0:
            return False
        queue=deque()
        queue.append((0,0))
        v=set()
        v.add((0,0))
        while queue:
            a,b=queue.popleft()
            if a==target or b==target or a+b==target:
                return True
            states=[]
            states.append((x,b))
            states.append((a,y))
            states.append((0,b))
            states.append((a,0))
            am=min(a,y-b)
            states.append((a-am,b+am))
            am=min(x-a,y)
            states.append((a+am,b-am))
            for i,j in states:
                if (i,j) not in v:
                    v.add((i,j))
                    queue.append((i,j))
        return False 