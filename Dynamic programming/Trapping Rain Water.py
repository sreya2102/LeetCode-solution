class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        water=left=right=0
        while(i<j):
            if height[i]<=height[j]:
                if height[i]>left:
                    left=height[i]
                else:
                    water=water+left-height[i]
                i=i+1
            else:
                if height[j]>right:
                    right=height[j]
                else:
                    water=water+right-height[j]
                j=j-1
        return water