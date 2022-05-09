TITLE = 'Rotate Array'
'''
time: BigO(k)
space: BigO(1)

Results:
    Runtime: 1272 ms, faster than 19.35%
    Memory Usage: 25.5 MB, less than 7.36%
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        while k:
            k -= 1
            nums.append(nums.pop(0))
        nums.reverse()