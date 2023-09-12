class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # brute force solution
        # time: O(n*m) where n is the number of cars and m is the total length of their ranges
        # space: O(m) where m is the total length of unique ints in their ranges
        count = set()
        for car in nums:
            count.update(range(car[0], car[1]+1))

        return len(count)