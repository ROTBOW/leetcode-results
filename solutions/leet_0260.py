TITLE = 'Single Number 3'
'''
time: BigO()
space: BigO()

Results:
    Runtime: 81 ms, faster than 57.30%
    Memory Usage: 16.2 MB, less than 13.83%
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
            else:
                result.remove(num)
        return list(result)
        