TITLE = 'Maximize the Topmost element after K moves'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 605 ms, faster than 91.05% of Python3 online submissions
    Memory Usage: 28 MB, less than 54.64% of Python3 online submissions
'''
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1 and k % 2 != 0:
            return -1
        
        if k >= len(nums) and (k % 2 == 0 or k >= 5):
            return max(nums)
        elif k >= len(nums) and k % 2 != 0:
            nums.pop()
            return max(nums)
        elif k == 0:
            return nums[0]
        elif k == 1:
            return nums[1]
        else:
            return max(*nums[:k-1], nums[k])