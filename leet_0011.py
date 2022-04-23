TITLE = 'Container With Most Water'
'''
leet_0011 wants us to find the container that can hold the most water in a list of heights

time: BigO(n)
space: BigO(1)

Results:
    Runtime: 676 ms, faster than 97.84%
    Memory Usage: 27.5 MB, less than 17.80%
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float('-inf')
        left, right = 0, len(height)-1
        for i in range(len(height)-1, 0, -1):
            if height[left] < height[right]:
                shortest_wall = height[left]
                left += 1
            else:
                shortest_wall = height[right]
                right -= 1
            max_water = max(max_water, shortest_wall * i)
        return max_water