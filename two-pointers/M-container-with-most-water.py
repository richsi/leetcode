#TWO POINTER METHOD

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxarea = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxarea = max(area, maxarea)

            if height[l] < height[r]:
                l += 1
            else: r -= 1

        return maxarea
    

#BRUTE FORCE METHOD
class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                if area > maxArea:
                    maxArea = area

        return maxArea
  