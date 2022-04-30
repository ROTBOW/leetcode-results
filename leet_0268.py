TITLE = 'Missing Number'
'''
time: BigO()
space: BigO()

Results:
    Runtime: 147 ms, faster than 77.97%
    Memory Usage: 15.8 MB, less than 7.31%
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)