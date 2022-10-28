from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        idx = 0
        
        for num in [0, 1, 2]:
            while count[num] != 0:
                nums[idx] = num
                count[num] -= 1
                idx += 1
                