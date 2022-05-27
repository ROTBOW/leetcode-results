TITLE = 'Number of Steps to Reduce Number to zero'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 27 ms, faster than 95.79%
    Memory Usage: 13.8 MB, less than 53.50%
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return count