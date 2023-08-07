class Solution:
    def maxArea(self, height: List[int]) -> int:
        wutermax = 0

        l, r = 0, len(height) - 1

        while l < r:
            wuter = (r - l) * min([height[l], height[r]])
            wutermax = max(wutermax, wuter)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return wutermax