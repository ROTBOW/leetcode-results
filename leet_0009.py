TITLE = 'palindrome number'
'''
leet_0002 is asking to check if the given interger is a palindrome.
I add the numbers to an list and check if it matches the reversed list.

time: BigO(n)
space: BigO(n)
'''



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        nums = []
        while x:
            nums.append(x % 10)
            x = x // 10
        return nums == nums[::-1]
            