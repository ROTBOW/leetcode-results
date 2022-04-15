TITLE = 'Container With Most Water'
'''
leet_0011 wants us to find the container that can hold the most water in a list of heights

time: BigO(n)
space: BigO(1)
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float('-inf')
        left, right = 0, len(height)-1
        while left < right:
            shortest_wall = min(height[left], height[right])
            max_water = max(max_water, shortest_wall * abs(left - right))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_water