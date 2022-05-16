TITLE = 'palindrome number'
'''
leet_0002 is asking to check if the given interger is a palindrome.
I add the numbers to an list and check if it matches the reversed list.

time: BigO(n)
space: BigO(n)

Results:
    Runtime: 70 ms, faster than 73.58%
    Memory Usage: 13.9 MB, less than 17.55%
'''



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        nums = []
        while x:
            nums.append(x % 10)
            x = x // 10
        return nums == nums[::-1]
            