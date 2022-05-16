TITLE = 'remove element'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 69 ms, faster than 7.35%
    Memory Usage: 14 MB, less than 13.92%
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        targets = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                targets.append(i)
        for target in targets:
            del nums[target]
        