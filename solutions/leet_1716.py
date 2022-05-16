TITLE = 'Calculate Money in Leetcode Bank'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 20 ms, faster than 87.23%
    Memory Usage: 13.5 MB, less than 42.55%
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        money, week = 0, 0
        
        while n > 0:
            week += 1
            for day in range(7):
                n -= 1
                money += day + week
                if n <= 0: break
                
        return money
    