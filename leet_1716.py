TITLE = 'Calculate Money in Leetcode Bank'
'''
time: BigO(n)
space: BigO(1)
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
    