class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxarea=0
        while(i<j):
            w=j-i
            area=min(height[i],height[j])*w
            maxarea=max(maxarea,area)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return maxarea
