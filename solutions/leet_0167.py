TITLE = 'Two Sum 2 - Input Array Is Sorted'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 197 ms, faster than 38.86%
    Memory Usage: 14.8 MB, less than 89.05%
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
                
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1