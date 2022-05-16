TITLE = 'two sum'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 64 ms, faster than 88.47% 
    Memory Usage: 15.5 MB, less than 9.31%
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = dict()
        
        for i in range(len(nums)):
            if nums[i] in storage.keys():
                return [i, storage[nums[i]]]
            storage[target - nums[i]] = i